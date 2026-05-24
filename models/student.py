from database.db import db

class Student(db.Model):

    __tablename__ = "students"

    # Unique ID
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Student Name
    student_name = db.Column(
        db.String(100),
        nullable=False
    )

    # DOB
    date_of_birth = db.Column(
        db.Date,
        nullable=False
    )

    # Age
    student_age = db.Column(
        db.Integer,
        nullable=False
    )

    # Gmail
    student_gmail = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    # Branch Dropdown
    student_branch = db.Column(
        db.Enum('CSE', 'ECE', 'IT', 'MECH'),
        nullable=False
    )