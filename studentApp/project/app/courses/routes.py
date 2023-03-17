from flask import request
from flask_jwt_extended import jwt_required
from app.courses.models import Course, Enrollment
from app import api, db

courses_ns = api.namespace('courses', description='Course operations')

@courses_ns.route('/')
class CoursesList(Resource):
    @jwt_required()
    def get(self):
        courses = Course.query.all()
        return {'courses': [course.__dict__ for course in courses]}, 200

    @jwt_required()
    def post(self):
        data = request.json
        course = Course(name=data['name'], course_id=data['course_id'], teacher=data['teacher'])
        db.session.add(course)
        db.session.commit()
        return {'message': 'Course created successfully'}, 201

@courses_ns.route('/<int:id>')
class CourseDetail(Resource):
    @jwt_required()
    def get(self, id):
        course = Course.query.get(id)
        if not course:
            return {'message': 'Course not found'}, 404
        return course.__dict__, 200

    @jwt_required()
    def put(self, id):
        course = Course.query.get(id)
        if not course:
            return {'message': 'Course not found'}, 404
        data = request.json
        course.name = data['name']
        course.course_id = data['course_id']
        course.teacher = data['teacher']
        db.session.commit()
        return {'message': 'Course updated successfully'}, 200

    @jwt_required()
    def delete(self, id):
        course = Course.query.get(id)
        if not course:
            return {'message': 'Course not found'}, 404
        db.session.delete(course)
        db.session.commit()
        return {'message': 'Course deleted successfully'}, 200

@courses_ns.route('/<int:course_id>/students')
class CourseStudentsList(Resource):
    @jwt_required()
    def get(self, course_id):
        course = Course.query.get(course_id)
        if not course:
            return {'message': 'Course not found'}, 404
        students = [enrollment.student.__dict__ for enrollment in course.enrollments]
        return {'students': students}, 200

@courses_ns.route('/<int:course_id>/enroll')
class CourseEnrollment(Resource):
    @jwt_required()
    def post(self, course_id):
        data = request.json
        student = Student.query.get(data['student_id'])
        course = Course.query.get(course_id)
        if not student or not course:
            return {'message': 'Invalid data provided'}, 400
        enrollment = Enrollment(student=student, course=course, grade=data['grade'])
        db.session.add(enrollment)
        db.session.commit()
        return {'message': 'Student enrolled in course successfully'}, 201

@courses_ns.route('/<int:course_id>/grades')
class CourseGrades(Resource):
    @jwt_required()
    def get(self, course_id):
        course = Course.query.get(course_id)
        if not course:
            return {'message': 'Course not found'}, 404
        grades = [{'student': enrollment.student.name, 'grade': enrollment.grade} for enrollment in course.enrollments]
        return {'grades': grades}, 200

