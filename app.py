from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Replace these values with your MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'anupam',
    'database': 'jb_table',
}

# Function to establish a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# API to display current week leaderboard (Top 200)
@app.route('/leaderboard/current_week', methods=['GET'])
def current_week_leaderboard():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
    SELECT UID, Name, Score, Country, TimeStamp
    FROM Leaderboard
    WHERE WEEK(TimeStamp) = WEEK(CURRENT_DATE())
    ORDER BY Score DESC
    LIMIT 200
    '''

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(results[0])

# API to display last week leaderboard given a country by the user (Top 200)
@app.route('/leaderboard/last_week/<country_code>', methods=['GET'])
def last_week_leaderboard(country_code):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = f'''
    SELECT UID, Name, Score, Country, TimeStamp
    FROM Leaderboard
    WHERE WEEK(TimeStamp) = WEEK(CURRENT_DATE()) - 1
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
    cursor = connection.cursor(dictionary=True)

    query = f'''
    SELECT UID, Name, Score, Country, TimeStamp,
    (SELECT COUNT(DISTINCT Score) FROM Leaderboard l2 WHERE l2.Score > l1.Score) + 1 AS `Rank`
    FROM Leaderboard l1
    WHERE UID = '{user_id}';
    '''


    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
