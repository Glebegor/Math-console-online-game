import flask
import sqlite3
from flask import jsonify, request
from flask_cors import CORS

# DB structure
# CREATE TABLE users (
#   id SERIAL PRIMARY KEY,
#   username TEXT NOT NULL,
#   password TEXT NOT NULL
# );

# CREATE TABLE statistic (
#     id SERIAL PRIMARY KEY,
#     user_id INTEGER NOT NULL,
#     count_of_wins INTEGER NOT NULL,
#     count_of_loses INTEGER NOT NULL,
#     count_of_games INTEGER NOT NULL,
#     biggest_number INTEGER NOT NULL,
#     win_streak INTEGER NOT NULL,
#     bigger_win_streak INTEGER NOT NULL,
#     rating INTEGER NOT NULL,

#     FOREIGN KEY (user_id) REFERENCES users (id)
# )


# App
app = flask.Flask(__name__)
def createConnection():
    conn = sqlite3.connect("main.db")
    conn.row_factory = sqlite3.Row  # This makes the results more dictionary-like
    return conn

# Route for auth
@app.route("/login", methods=["POST"])
def login():
    json_data = request.json
    username = json_data["username"]
    password = json_data["password"]
    with createConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            return jsonify({"message": "Success"})
        else:
            return jsonify({"message": "Fail"}), 401  # Use 401 for unauthorized
@app.route("/register", methods=["POST"])
def register():
    json_data = request.json
    username = json_data["username"]
    password = json_data["password"]
    with createConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        cursor.execute("INSERT INTO statistic (user_id, count_of_wins, count_of_loses, count_of_games, biggest_number, win_streak, bigger_win_streak, rating) VALUES (?, 0, 0, 0, 0, 0, 0, 0)", (cursor.lastrowid,))
        conn.commit()  
    return jsonify({"message": "Success"}), 201  

# Route for statistic
@app.route("/statistic/<name>", methods=["GET"])
def statistic(name):
    with createConnection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = ?", (name,))
        user = cursor.fetchone()

        if user:
            cursor.execute("SELECT * FROM statistic WHERE user_id = ?", (user["id"],))
            statistic = cursor.fetchone()

            if statistic:
                return jsonify(dict(statistic))
            else:
                return jsonify({"message": "Statistic not found"}), 404
        else:
            return jsonify({"message": "User not found"}), 404


# Rooms
@app.route("/rooms", methods=["GET"])
def getRooms():
    with createConnection() as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM rooms")
        rooms = cursor.fetchall()

        return jsonify(dict(rooms))

if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run(debug=True)
