from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database (list)
students = []
student_id_counter = 1

@app.route('/')
def hello():
    return "Welcome to the Students API!"


# ✅ CREATE Student
@app.route('/students', methods=['POST'])
def create_student():
    global student_id_counter
    data = request.json

    student = {
        "id": student_id_counter,
        "name": data.get("name"),
        "age": data.get("age"),
        "course": data.get("course")
    }

    students.append(student)
    student_id_counter += 1

    return jsonify({
        "message": "Student created successfully",
        "student": student
    }), 201


# ✅ READ All Students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200


# ✅ READ Single Student
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


# ✅ UPDATE Student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json

    for student in students:
        if student["id"] == id:
            student["name"] = data.get("name", student["name"])
            student["age"] = data.get("age", student["age"])
            student["course"] = data.get("course", student["course"])

            return jsonify({
                "message": "Student updated successfully",
                "student": student
            }), 200

    return jsonify({"error": "Student not found"}), 404


# ✅ DELETE Student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"}), 200

    return jsonify({"error": "Student not found"}), 404


# ✅ HEALTH CHECK (for Jenkins later)
@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "UP",
        "service": "students-api"
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
