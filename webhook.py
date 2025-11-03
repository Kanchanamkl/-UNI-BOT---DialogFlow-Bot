from flask import Flask, request, jsonify
from database import Database
from datetime import datetime
import os

app = Flask(__name__)
db = Database()

def format_time(time_str):
    """Convert 24hr time to 12hr format"""
    try:
        time_obj = datetime.strptime(str(time_str), '%H:%M:%S')
        return time_obj.strftime('%I:%M %p')
    except:
        return str(time_str)

def format_lectures_response(lectures, program, year_level, day_name):
    """Format lectures into a readable response"""
    if not lectures:
        return f"You don't have any lectures scheduled for {day_name.capitalize()}. 📅\n\nEnjoy your free day! 🎉"
    
    # Build response
    day_display = day_name.capitalize()
    response = f"📚 Here are your lectures for {day_display}:\n\n"
    
    for idx, lecture in enumerate(lectures, 1):
        start = format_time(lecture['start_time'])
        end = format_time(lecture['end_time'])
        
        response += f"{'='*50}\n"
        response += f"LECTURE {idx}: {lecture['title']} ({lecture['course_code']})\n"
        response += f"⏰ Time: {start} - {end}\n"
        response += f"📍 Venue: {lecture['venue']}\n"
        response += f"📖 Topic: {lecture['topic']}\n"
        response += f"{'='*50}\n\n"
    
    return response.strip()

def handle_schedule_query(parameters, contexts):
    """
    Main handler for schedule queries
    Manages conversation flow and context
    """
    program = parameters.get('program')
    year_level = parameters.get('year_level')
    day_query = parameters.get('day_query', 'today')  # Default to 'today'
    
    # Check if we have all required information
    if not program and not year_level:
        # Ask for program first
        return {
            'fulfillmentText': "I'd be happy to show you your lecture schedule! 📅\n\nFirst, what program are you studying? (e.g., Computer Science, Software Engineering, Information Technology)",
            'outputContexts': [
                {
                    'name': f"{contexts[0]['name'].split('/contexts/')[0]}/contexts/awaiting-program",
                    'lifespanCount': 5,
                    'parameters': {
                        'day_query': day_query
                    }
                }
            ]
        }
    
    elif program and not year_level:
        # We have program, ask for year
        return {
            'fulfillmentText': f"Great! You're studying {program}. 🎓\n\nWhat year level are you in? (1st, 2nd, 3rd, or 4th year)",
            'outputContexts': [
                {
                    'name': f"{contexts[0]['name'].split('/contexts/')[0]}/contexts/awaiting-year",
                    'lifespanCount': 5,
                    'parameters': {
                        'program': program,
                        'day_query': day_query
                    }
                }
            ]
        }
    
    else:
        # We have both program and year - fetch lectures
        weekday = db.get_day_name(day_query)
        lectures = db.get_lectures_by_day(program, int(year_level), weekday)
        response_text = format_lectures_response(lectures, program, year_level, weekday)
        
        return {
            'fulfillmentText': response_text
        }

@app.route('/webhook', methods=['POST'])
def webhook():
    """Main webhook endpoint for Dialogflow"""
    try:
        req = request.get_json(force=True)
        
        # Extract data from Dialogflow request
        intent_name = req.get('queryResult').get('intent').get('displayName')
        parameters = req.get('queryResult').get('parameters')
        contexts = req.get('queryResult').get('outputContexts', [])
        action = req.get('queryResult').get('action')
        
        print(f"Intent: {intent_name}")
        print(f"Action: {action}")
        print(f"Parameters: {parameters}")
        
        # Route to appropriate handler based on intent/action
        if intent_name == 'Schedule.Query' or action == 'query.schedule':
            response = handle_schedule_query(parameters, contexts)
        
        elif intent_name == 'Schedule.Query.ProvideProgram' or action == 'provide.program':
            # Get day_query from context if exists
            day_query = 'today'
            for context in contexts:
                if 'awaiting-program' in context.get('name', ''):
                    day_query = context.get('parameters', {}).get('day_query', 'today')
            
            parameters['day_query'] = day_query
            response = handle_schedule_query(parameters, contexts)
        
        elif intent_name == 'Schedule.Query.ProvideYear' or action == 'provide.year':
            # Get program and day_query from context
            program = None
            day_query = 'today'
            
            for context in contexts:
                if 'awaiting-year' in context.get('name', ''):
                    program = context.get('parameters', {}).get('program')
                    day_query = context.get('parameters', {}).get('day_query', 'today')
            
            parameters['program'] = program
            parameters['day_query'] = day_query
            response = handle_schedule_query(parameters, contexts)
        
        elif intent_name == 'Schedule.Query.Complete' or action == 'query.complete':
            response = handle_schedule_query(parameters, contexts)
        
        else:
            response = {
                'fulfillmentText': "I'm here to help with your lecture schedule! Just ask me 'What are my lectures today?'"
            }
        
        return jsonify(response)
    
    except Exception as e:
        print(f"Error in webhook: {e}")
        return jsonify({
            'fulfillmentText': "Sorry, I encountered an error. Please try again."
        })

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Webhook is running'})

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'service': 'University Chatbot Webhook',
        'status': 'running',
        'endpoints': {
            'webhook': '/webhook',
            'health': '/health'
        }
    })

if __name__ == '__main__':
    # Connect to database on startup
    db.connect()
    
    # Run Flask app
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)