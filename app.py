from flask import Flask, render_template, request, jsonify
from db import conn, cursor

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Add Student API
@app.route("/add_student", methods=["POST"])
def add_student():

    data = request.get_json()

    name = data["name"]
    age = data["age"]

    query = "INSERT INTO students (name, age) VALUES (%s, %s)"

    values = (name, age)

    cursor.execute(query, values)

    conn.commit()

    return jsonify({
        "message": "Student Added Successfully"
    })

# Get Students API
@app.route("/students", methods=["GET"])
def get_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    result = []

    for student in students:

        result.append({
            "id": student[0],
            "name": student[1],
            "age": student[2]
        })

    return jsonify(result)

app.run(debug=True)