# import mysql.connector
# from faker import Faker
# from datetime import datetime, timedelta

# # Replace these values with your MySQL database credentials
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'anupam',
#     'database': 'jb_table',
# }

# # Function to establish a database connection
# def get_db_connection():
#     return mysql.connector.connect(**db_config)

# # Function to create fake data
# def generate_fake_data(num_entries):
#     fake = Faker()
#     fake_data = []

#     for _ in range(num_entries):
#         uid = fake.uuid4()
#         name = fake.name()
#         score = fake.random_int(min=0, max=1000)
#         country = fake.country_code()
#         timestamp = datetime.now() - timedelta(days=fake.random_int(min=0, max=365))

#         fake_data.append((uid, name, score, country, timestamp))

#     return fake_data

# # Function to insert fake data into the database
# def insert_fake_data(fake_data):
#     connection = get_db_connection()
#     cursor = connection.cursor()

#     insert_query = '''
#     INSERT INTO Leaderboard (UID, Name, Score, Country, TimeStamp)
#     VALUES (%s, %s, %s, %s, %s)
#     '''

#     cursor.executemany(insert_query, fake_data)

#     connection.commit()
#     cursor.close()
#     connection.close()

# if __name__ == '__main__':
#     # Specify the number of fake entries to generate
#     num_entries = 9800

#     # Generate fake data
#     fake_data = generate_fake_data(num_entries)

#     # Insert fake data into the database
#     insert_fake_data(fake_data)

#     print(f'{num_entries} fake entries inserted into the Leaderboard table.')
import psycopg2
from faker import Faker
from datetime import datetime, timedelta

# Replace these values with your PostgreSQL database credentials
db_config_postgres = {
    'host': 'localhost',
    'user': 'your_postgres_user',
    'password': 'your_postgres_password',
    'database': 'your_postgres_database',
}

# Function to establish a database connection
def get_db_connection():
    return psycopg2.connect(**db_config_postgres)

# Function to create fake data
def generate_fake_data(num_entries):
    fake = Faker()
    fake_data = []

    for _ in range(num_entries):
        uid = fake.uuid4()
        name = fake.name()
        score = fake.random_int(min=0, max=1000)
        country = fake.country_code()
        timestamp = datetime.now() - timedelta(days=fake.random_int(min=0, max=365))

        fake_data.append((uid, name, score, country, timestamp))

    return fake_data

# Function to insert fake data into the database
def insert_fake_data(fake_data):
    connection = get_db_connection()
    cursor = connection.cursor()

    insert_query = '''
    INSERT INTO Leaderboard (UID, Name, Score, Country, TimeStamp)
    VALUES (%s, %s, %s, %s, %s)
    '''

    cursor.executemany(insert_query, fake_data)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    # Specify the number of fake entries to generate
    num_entries = 9800

    # Generate fake data
    fake_data = generate_fake_data(num_entries)

    # Insert fake data into the database
    insert_fake_data(fake_data)

    print(f'{num_entries} fake entries inserted into the Leaderboard table.')
