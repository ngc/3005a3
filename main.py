import psycopg2
import os
from dotenv import load_dotenv
from init_db import init_db

# Load environment variables
load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


def connect_db():
    """Connect to the PostgreSQL database server."""
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn


def getAllStudents():
    """Retrieve and display all records from the students table."""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    student_records = cur.fetchall()
    for row in student_records:
        print(row)
    cur.close()
    conn.close()
