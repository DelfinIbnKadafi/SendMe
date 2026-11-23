import os
from dotenv import load_dotenv
from flask import *
import mysql.connector
import sys
from hashlib import sha256

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
    sys.exit()

cursor = db.cursor(dictionary=True)
###############################################

## hash functions
def hashing(input):
    return sha256(input.encode('utf-8')).hexdigest()

# auth
## Login
@app.post("/login")
def login():

    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # check if username is exist
    cursor.execute("SELECT * FROM user WHERE email = %s", (email,))

    row = cursor.fetchone()

    if row is None:
        return jsonify({"status": "undefined_user"})
    else:
        if hashing(password) != row["password"]:
            return jsonify({"status": "password_wrong"})
        else:
            return jsonify({"status": "succes"})

    return jsonify({"status": "error"})


if __name__ == "__main__":
    app.run(debug=True, port=7777)