# from flask import Flask, jsonify, request
# import mysql.connector

# app = Flask(__name__)

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

# # API to display current week leaderboard (Top 200)
# @app.route('/leaderboard/current_week', methods=['GET'])
# def current_week_leaderboard():
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)

#     query = '''
#     SELECT UID, Name, Score, Country, TimeStamp
#     FROM Leaderboard
#     WHERE WEEK(TimeStamp) = WEEK(CURRENT_DATE())
#     ORDER BY Score DESC
#     LIMIT 200
#     '''

#     cursor.execute(query)
#     results = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     return jsonify(results[0])

# # API to display last week leaderboard given a country by the user (Top 200)
# @app.route('/leaderboard/last_week/<country_code>', methods=['GET'])
# def last_week_leaderboard(country_code):
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)

#     query = f'''
#     SELECT UID, Name, Score, Country, TimeStamp
#     FROM Leaderboard
#     WHERE WEEK(TimeStamp) = WEEK(CURRENT_DATE()) - 1
#     AND Country = '{country_code}'
#     ORDER BY Score DESC
#     LIMIT 200
#     '''

#     cursor.execute(query)
#     results = cursor.fetchall()

#     cursor.close()
#     connection.close()

#     return jsonify(results)

# # API to fetch user rank, given the userId
# @app.route('/user/rank/<user_id>', methods=['GET'])
# def user_rank(user_id):
#     connection = get_db_connection()
#     cursor = connection.cursor(dictionary=True)

#     query = f'''
#     SELECT UID, Name, Score, Country, TimeStamp,
#     (SELECT COUNT(DISTINCT Score) FROM Leaderboard l2 WHERE l2.Score > l1.Score) + 1 AS `Rank`
#     FROM Leaderboard l1
#     WHERE UID = '{user_id}';
#     '''


#     cursor.execute(query)
#     result = cursor.fetchone()

#     cursor.close()
#     connection.close()

#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')

# Check if any of the environment variables are missing
if None in [DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE]:
    raise ValueError("Please set the environment variables for database connection.")


# Replace these values with your PostgreSQL database credentials
db_config_postgres = {
    'host': 'dpg-cmomal6d3nmc739mj0qg-a.oregon-postgres.render.com',
    'user': 'user',
    # 'password': 'eCLDVvK3pvG4dYlN7UzN3vAJcRLYYAgs',
    'password': DB_PASSWORD,
    'database': 'your_postgres_database',
}

db_config_postgres = {
    'host': DB_HOST,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'database': DB_DATABASE,
}

# Function to establish a database connection
def get_db_connection():
    return psycopg2.connect(**db_config_postgres)

# API to display current week leaderboard (Top 200)
@app.route('/leaderboard/current_week', methods=['GET'])
def current_week_leaderboard():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = '''
    SELECT UID, Name, Score, Country, TimeStamp
    FROM Leaderboard
    WHERE EXTRACT(WEEK FROM TimeStamp) = EXTRACT(WEEK FROM CURRENT_DATE)
    ORDER BY Score DESC
    LIMIT 200
    '''

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(results)

# API to display last week leaderboard given a country by the user (Top 200)
@app.route('/leaderboard/last_week/<country_code>', methods=['GET'])
def last_week_leaderboard(country_code):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = f'''
    SELECT UID, Name, Score, Country, TimeStamp
    FROM Leaderboard
    WHERE EXTRACT(WEEK FROM TimeStamp) = EXTRACT(WEEK FROM CURRENT_DATE) - 1
    AND Country = '{country_code}'
    ORDER BY Score DESC
    LIMIT 200
    '''

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(results)

# API to fetch user rank, given the userId
@app.route('/user/rank/<user_id>', methods=['GET'])
def user_rank(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = f'''
    SELECT UID, Name, Score, Country, TimeStamp,
    (SELECT COUNT(DISTINCT Score) FROM Leaderboard l2 WHERE l2.Score > l1.Score) + 1 AS "Rank"
    FROM Leaderboard l1
    WHERE UID = '{user_id}';
    '''

    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return jsonify(result)

def create_app():
    app.run(debug=True)
    return app
