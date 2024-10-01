import flask 
import sqlite3
from flask import jsonify

app = flask.Flask(__name__)

def createConnection():
    return sqlite3.connect("main.db")

def createCursor():
    return createConnection().cursor()


returnType = "application/json"

@app.route("/", methods=["GET"])
def index():
    return "Hello, World!"

@app.route("/login", methods=["POST"])
def login():
    json = flask.request.json
    username = json["username"]
    password = json["password"]

    cursor = createCursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        return jsonify({"message": "Success"})
    else:
        return jsonify({"message": "Fail"})


@app.route("/register", methods=["POST"])
def register():
    json = flask.request.json
    username = json["username"]
    password = json["password"]
    
    cursor = createCursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    return jsonify({"message": "Success"})
    


if __name__ == "__main__":
    # cors all
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['CORS_RESOURCES'] = {r"/*": {"origins": "*"}}
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    app.config['CORS_EXPOSE_HEADERS'] = "Content-Type"
    app.config['CORS_AUTOMATIC_OPTIONS'] = True
    
    app.run(debug=True)
