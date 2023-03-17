from flask import request
from flask_jwt_extended import jwt_required
from app.students.models import Student, Course, Enrollment
from app import api, db

students_ns = api.namespace('students', description='Student operations')

@students_ns.route('/')
class StudentsList(Resource):
    @jwt_required()
    def get(self):
        students = Student.query.all()
        return {'students': [student.__dict__ for student in students]}, 200

    @jwt_required()
    def post(self):
        data = request.json
        student = Student(name=data['name'], student_id=data['student_id'], email=data['email'])
        db.session.add(student)
        db.session.commit()
        return {'message': 'Student created successfully'}, 201

@students_ns.route('/<int:id>')
class StudentDetail(Resource):
    @jwt_required()
    def get(self, id):
        student = Student.query.get(id)
        if not student:
            return {'message': 'Student not found'}, 404
        return student.__dict__, 200

    @jwt_required()
    def put(self, id):
        student = Student.query.get(id)
        if not student:
            return {'message': 'Student not found'}, 404
        data = request.json
        student.name = data['name']
        student.student_id = data['student_id']
        student.email = data['email']
        db.session.commit()
        return {'message': 'Student updated successfully'}, 200

    @jwt_required()
    def delete(self, id):
        student = Student.query.get(id)
        if not student:
            return {'message': 'Student not found'}, 404
        db.session.delete(student)
        db.session.commit()
        return {'message': 'Student deleted successfully'}, 200
