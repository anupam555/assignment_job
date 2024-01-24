import mysql.connector

# Replace these values with your MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'anupam',
    'database': 'jb_table',
}

# Connect to the MySQL server
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create the table
create_table_query = '''
CREATE TABLE Leaderboard (
    UID VARCHAR(255) PRIMARY KEY,
    Name VARCHAR(255),
    Score INT,
    Country VARCHAR(2),
    TimeStamp TIMESTAMP
)
'''

cursor.execute(create_table_query)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()
