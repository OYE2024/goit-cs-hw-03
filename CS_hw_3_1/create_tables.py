import psycopg2

db_config = {
    "dbname": "postgres-db",
    "user": "postgres",
    "password": "qwerty",
    "host": "localhost",
    "port": 5432,
    "options": "-c client_encoding=UTF8"
}

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
        # підключення до бази даних
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        # створення таблиць
        for command in create_tables_commands:
            cur.execute(command)
        # завершення транзакції
        conn.commit()
        print("Tables were created successfully.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
