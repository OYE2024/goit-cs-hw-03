import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

AIVEN_URL = os.getenv("AIVEN_PASSWORD")

if not AIVEN_URL:
    raise ValueError("Змінна оточення AIVEN_PASSWORD не встановлена!")

create_tables_commands = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        status_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (status_id) REFERENCES status(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """
]


def create_tables():
    conn = None
    try:
        conn = psycopg2.connect(AIVEN_URL)

        cur = conn.cursor()

        cur.execute('SELECT VERSION()')
        version = cur.fetchone()[0]
        print(f"Connected to: {version}")

        for command in create_tables_commands:
            cur.execute(command)

        conn.commit()
        print("Tables were created successfully.")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Database error: {error}")
    finally:
        if conn is not None:
            conn.close()
            print("Connection closed.")


if __name__ == '__main__':
    create_tables()
