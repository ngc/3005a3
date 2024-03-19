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


def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a new student record into the students table."""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
        (first_name, last_name, email, enrollment_date),
    )
    conn.commit()
    print("Student added successfully.")
    cur.close()
    conn.close()


def updateStudentEmail(student_id, new_email):
    """Update the email address for a student with the specified student_id."""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id)
    )
    conn.commit()
    print("Student email updated successfully.")
    cur.close()
    conn.close()


def deleteStudent(student_id):
    """Delete the record of the student with the specified student_id."""
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    conn.commit()
    print("Student deleted successfully.")
    cur.close()
    conn.close()
