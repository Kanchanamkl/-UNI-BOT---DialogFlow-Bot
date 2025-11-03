import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv('DB_HOST', 'localhost')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.connection = None
    
    def connect(self):
        """Create database connection"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Successfully connected to MySQL database")
                return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")
    
    def get_lectures_by_day(self, program, year_level, weekday):
        """
        Get lectures for specific program, year, and day
        
        Args:
            program (str): Program name (e.g., 'Computer Science')
            year_level (int): Year level (1, 2, 3, or 4)
            weekday (str): Day of week (e.g., 'monday')
        
        Returns:
            list: List of lecture dictionaries
        """
        if not self.connection or not self.connection.is_connected():
            self.connect()
        
        try:
            cursor = self.connection.cursor(dictionary=True)
            
            query = """
                SELECT 
                    course_code,
                    title,
                    start_time,
                    end_time,
                    venue,
                    topic,
                    weekday
                FROM lectures
                WHERE program = %s 
                AND year_level = %s 
                AND weekday = %s
                ORDER BY start_time
            """
            
            cursor.execute(query, (program, year_level, weekday.lower()))
            lectures = cursor.fetchall()
            cursor.close()
            
            return lectures
            
        except Error as e:
            print(f"Error fetching lectures: {e}")
            return []
    
    def get_day_name(self, day_query):
        """
        Convert day query to actual weekday name
        
        Args:
            day_query (str): 'today', 'tomorrow', or day name
        
        Returns:
            str: Weekday name in lowercase
        """
        from datetime import datetime, timedelta
        
        if day_query == 'today':
            return datetime.now().strftime('%A').lower()
        elif day_query == 'tomorrow':
            tomorrow = datetime.now() + timedelta(days=1)
            return tomorrow.strftime('%A').lower()
        else:
            # Already a day name (monday, tuesday, etc.)
            return day_query.lower()

# Test function
if __name__ == "__main__":
    db = Database()
    if db.connect():
        # Test query
        lectures = db.get_lectures_by_day('Computer Science', 2, 'monday')
        print(f"Found {len(lectures)} lectures:")
        for lecture in lectures:
            print(lecture)
        db.disconnect()