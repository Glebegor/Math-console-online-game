import flask
import sqlite3
from flask import jsonify, request
from flask_cors import CORS

app = flask.Flask(__name__)

# Enable CORS with the proper configuration
CORS(app, supports_credentials=True)

# Function to create a database connection
def createConnection():
    conn = sqlite3.connect("main.db")
    conn.row_factory = sqlite3.Row  # This makes the results more dictionary-like
    return conn

# Route for a simple index page
@app.route("/", methods=["GET"])
def index():
    return "Hello, World!"

# Route for user login
@app.route("/login", methods=["POST"])
def login():
    json_data = request.json
    username = json_data["username"]
    password = json_data["password"]

    # Open a connection and a cursor
    with createConnection() as conn:
        cursor = conn.cursor()
        # Execute the query to find the user
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        
        # Check if the user was found and return the appropriate message
        if user:
            return jsonify({"message": "Success"})
        else:
            return jsonify({"message": "Fail"}), 401  # Use 401 for unauthorized

# Route for user registration
@app.route("/register", methods=["POST"])
def register():
    json_data = request.json
    username = json_data["username"]
    password = json_data["password"]
    
    # Open a connection and a cursor
    with createConnection() as conn:
        cursor = conn.cursor()
        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()  # Commit the changes to the database
    
    return jsonify({"message": "Success"}), 201  # 201 for created

if __name__ == "__main__":
    app.run(debug=True)
