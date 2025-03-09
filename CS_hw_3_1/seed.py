from faker import Faker
import psycopg2
import random

fake = Faker()

db_config = {
    "dbname": "postgresdb",
    "user": "postgres",
    "password": "qwerty",
    "host": "localhost",
    "port": 5432,
}


def generate_users(n=10):
    users = [(fake.name(), fake.email()) for _ in range(n)]
    return users


def generate_statuses():
    statuses = [('new',), ('in progress',), ('completed',)]
    return statuses


def generate_tasks(n=30):
    tasks = [(fake.sentence(nb_words=4), fake.text(), random.randint(
        1, 3), random.randint(1, 10)) for _ in range(n)]
    return tasks


def populate_database():
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        users = generate_users()
        cur.executemany(
            "INSERT INTO users (name, email) VALUES (%s, %s)", users)

        statuses = generate_statuses()
        cur.executemany("INSERT INTO status (name) VALUES (%s)", statuses)

        tasks = generate_tasks()
        cur.executemany(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", tasks)

        conn.commit()
        print("Data was added successfully.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    populate_database()
