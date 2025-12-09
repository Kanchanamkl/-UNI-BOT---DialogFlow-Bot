# University Chatbot - Lecture Schedule & Resources

A Dialogflow-powered chatbot that helps students access their lecture schedules and course materials.

## Features

- 📅 **Lecture Schedule Queries**: Get your daily lecture schedule
- 📚 **Course Resources**: Access lecture notes and materials by subject and week
- 🔍 **Smart Context Management**: Conversational flow for missing information
- 🎯 **Multi-course Support**: Databases, Digital Forensics, Distributed & Cloud Systems

## New Resource Query Feature

Students can now ask for course materials:
- "Show me lecture notes for Databases week 3"
- "I need materials for Digital Forensics"
- "Get me week 5 resources for DCSP"

### Supported Courses:
1. **Distributed and Cloud System Programming (DCSP)** - Weeks 1-4
2. **Databases (DB)** - Weeks 1-6
3. **Digital Forensics (DF)** - Weeks 1-7

## Setup Instructions

### 1. Database Setup

Run the initialization script:
```bash
mysql -u root -p < init_database.sql
```

### 2. Install Dependencies

```bash
pip install flask mysql-connector-python
```

### 3. Configure Database

Update `database.py` with your MySQL credentials.

### 4. Dialogflow Setup

Import the intents from `dialogflow_intents.md`:
- Resources.Query
- Resources.ProvideCourse
- Resources.ProvideWeek

Set webhook URL to: `https://your-domain.com/webhook`

### 5. Run the Application

```bash
python webhook.py
```

## API Endpoints

- `POST /webhook` - Dialogflow fulfillment endpoint
- `GET /health` - Health check
- `GET /` - Service information

## Database Schema

### course_resources
- `id` - Primary key
- `course_code` - Course identifier (DCSP, DB, DF)
- `course_name` - Full course name
- `week_number` - Week number (1-12)
- `resource_title` - Title of the resource
- `resource_url` - Canvas URL to the resource
- `resource_order` - Order within the week

## Example Usage

**Get specific week resources:**
```
User: "Show me Databases week 3 notes"
Bot: [Lists all week 3 resources with links]
```

**Browse all resources:**
```
User: "I need lecture materials"
Bot: "Which course are you looking for?"
User: "Digital Forensics"
Bot: "Which week's materials do you need?"
User: "Week 5"
Bot: [Shows week 5 resources]
```

## Contributing

1. Add new courses to `init_database.sql`
2. Update course mappings in `webhook.py`
3. Add corresponding Dialogflow intents

## License

MIT License
