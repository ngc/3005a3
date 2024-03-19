import psycopg2
import os
from dotenv import load_dotenv


def init_db():
    load_dotenv()
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")

    # Connect to the database
    conn = psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
    )

    cur = conn.cursor()

    check_table_exists = """
    SELECT EXISTS (
        SELECT FROM pg_tables
        WHERE schemaname = 'public'
        AND tablename  = 'students'
    );
    """

    create_table = """
    CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        enrollment_date DATE
    );
    """

    insert_data = """
    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
    """

    cur.execute(check_table_exists)
    table_exists = cur.fetchone()[0]
    if not table_exists:
        print("Creating table and inserting initial data...")
        cur.execute(create_table)
        cur.execute(insert_data)
        print("Table created and data inserted successfully.")
    else:
        print("Table 'students' already exists. Skipping creation and initialization.")

    cur.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
