import flask
import sqlite3
from flask import jsonify, request
from flask_cors import CORS

# DB structure
# CREATE TABLE users (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Use AUTOINCREMENT for SQLite
#   username TEXT NOT NULL UNIQUE,  -- Adding UNIQUE constraint to ensure no duplicate usernames
#   password TEXT NOT NULL,
#   isAdmin BOOLEAN NOT NULL DEFAULT 0
# );

# CREATE TABLE statistic (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Use AUTOINCREMENT for SQLite
#     user_id INTEGER NOT NULL,
#     count_of_wins INTEGER NOT NULL DEFAULT 0,
#     count_of_loses INTEGER NOT NULL DEFAULT 0,
#     count_of_games INTEGER NOT NULL DEFAULT 0,
#     biggest_number INTEGER NOT NULL DEFAULT 0,
#     win_streak INTEGER NOT NULL DEFAULT 0,
#     bigger_win_streak INTEGER NOT NULL DEFAULT 0,
#     rating INTEGER NOT NULL DEFAULT 0,
#     FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE  -- Enforce referential integrity
# );

# CREATE TABLE rooms (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Use AUTOINCREMENT for SQLite
#     name TEXT NOT NULL,
#     playerName1 TEXT NOT NULL,
#     playerName2 TEXT,
#     balance INTEGER NOT NULL DEFAULT 10000
# );




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
        return jsonify([dict(room) for room in rooms])
    
@app.route("/rooms", methods=["POST"])
def createRoom():
    json_data = request.json
    name = json_data["name"]
    playerName = json_data["playerName"]
    balance = json_data["balance"]
    with createConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO rooms (name, playerName1, balance) VALUES (?, ?, ?)", (name, playerName, balance))
        conn.commit()  
    return jsonify({"message": "Success"}), 201

if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run(debug=True, port=6000)
