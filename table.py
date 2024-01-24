# import mysql.connector

# # Replace these values with your MySQL database credentials
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'anupam',
#     'database': 'jb_table',
# }

# # Connect to the MySQL server
# connection = mysql.connector.connect(**db_config)
# cursor = connection.cursor()

# # Create the table
# create_table_query = '''
# CREATE TABLE Leaderboard (
#     UID VARCHAR(255) PRIMARY KEY,
#     Name VARCHAR(255),
#     Score INT,
#     Country VARCHAR(2),
#     TimeStamp TIMESTAMP
# )
# '''

# cursor.execute(create_table_query)

# # Commit the changes and close the connection
# connection.commit()
# cursor.close()
# connection.close()

import psycopg2

# Replace these values with your PostgreSQL database credentials
db_config_postgres = {
    'host': 'localhost',
    'user': 'your_postgres_user',
    'password': 'your_postgres_password',
    'database': 'your_postgres_database',
}

# Connect to the PostgreSQL server
connection_postgres = psycopg2.connect(**db_config_postgres)
cursor_postgres = connection_postgres.cursor()

# Create the table with PostgreSQL-compatible syntax
create_table_query_postgres = '''
CREATE TABLE Leaderboard (
    UID VARCHAR(255) PRIMARY KEY,
    Name VARCHAR(255),
    Score INTEGER,
    Country VARCHAR(2),
    TimeStamp TIMESTAMPTZ
);
'''

cursor_postgres.execute(create_table_query_postgres)

# Commit the changes and close the connection
connection_postgres.commit()
cursor_postgres.close()
connection_postgres.close()
