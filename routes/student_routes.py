from flask import Blueprint, request, jsonify
from models.student import Student
from database.db import db
import re
from datetime import datetime

student_bp = Blueprint("student_bp", __name__)

gmail_pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.(com|in)$'


@student_bp.route('/add-student', methods=['POST'])
def add_student():

    data = request.get_json()

    # Gmail Validation
    if not re.match(gmail_pattern, data['student_gmail']):
        return jsonify({
            "error": "Only Gmail accounts allowed"
        }), 400

    # Age Validation
    if not isinstance(data['student_age'], int):
        return jsonify({
            "error": "Age must be integer"
        }), 400

    # Convert Date
    dob = datetime.strptime(
        data['date_of_birth'],
        "%Y-%m-%d"
    ).date()

    student = Student(
        student_name=data['student_name'],
        date_of_birth=dob,
        student_age=data['student_age'],
        student_gmail=data['student_gmail'],
        student_branch=data['student_branch']
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({
        "message": "Student Added Successfully"
    })


@student_bp.route('/students', methods=['GET'])
def get_students():

    students = Student.query.all()

    result = []

    for student in students:

        result.append({

            "id": student.id,

            "student_name": student.student_name,

            "date_of_birth": str(student.date_of_birth),

            "student_age": student.student_age,

            "student_gmail": student.student_gmail,

            "student_branch": student.student_branch
        })

    return jsonify({

        "total_students": len(result),

        "students": result
    })