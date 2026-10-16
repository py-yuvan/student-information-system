
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_student():
    student = {
        "name": request.form["name"],
        "student_id": request.form["student_id"],
        "email": request.form["email"]
    }
    students.append(student)
    return redirect("/students")

@app.route("/students")
def view_students():
    return render_template("students.html", students=students)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        student_id = request.form["student_id"]

        for student in students:
            if student["student_id"] == student_id:
                return f"Welcome, {student['name']}! Login successful."

        return "Student ID not found. Please register first."

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
