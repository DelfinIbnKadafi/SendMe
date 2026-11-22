import os
from dotenv import load_dotenv
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# connect to database
load_dotenv()
try:
    db = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("db"),
    )
    if db.is_connected():
        print("MySQL connected successfully!")
except mysql.connector.Error as error:
    print(f"MySQL connection failed: {error}")
    db = None
###############################################

# auth
## Login
@app.post("/login")
def login():
    return jsonify({"status": "error"})


if __name__ == "__main__":
    app.run(debug=True, port=7777)