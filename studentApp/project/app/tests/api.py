import json
import unittest

from run import app, db
from app.students.models import Student
from app.courses.models import Course, Enrollment


class APITestCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['TESTING'] = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
            self.create_test_data()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def create_test_data(self):
        student1 = Student(name='John Doe', student_id='1001', email='john.doe@example.com')
        student2 = Student(name='Jane Smith', student_id='1002', email='jane.smith@example.com')
        db.session.add_all([student1, student2])
        db.session.commit()

        course1 = Course(name='Introduction to Computer Science', course_id='CS101', teacher='Dr. Smith')
        course2 = Course(name='Web Development', course_id='CS201', teacher='Prof. Johnson')
        db.session.add_all([course1, course2])
        db.session.commit()

        enrollment1 = Enrollment(student=student1, course=course1, grade=85)
        enrollment2 = Enrollment(student=student1, course=course2, grade=90)
        enrollment3 = Enrollment(student=student2, course=course2, grade=75)
        db.session.add_all([enrollment1, enrollment2, enrollment3])
        db.session.commit()

    def test_create_student(self):
        response = self.app.post('/api/students', data=json.dumps({
            'name': 'Test Student',
            'student_id': '1003',
            'email': 'test.student@example.com'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Student created successfully')
        self.assertTrue('id' in data)

    def test_get_students(self):
        response = self.app.get('/api/students')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(len(data['students']) == 2)

    def test_get_student(self):
        response = self.app.get('/api/students/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'John Doe')

    def test_update_student(self):
        response = self.app.put('/api/students/1', data=json.dumps({
            'name': 'Updated Student',
            'student_id': '1001',
            'email': 'john.doe.updated@example.com'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Student updated successfully')

    def test_delete_student(self):
        response = self.app.delete('/api/students/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Student deleted successfully')

    def test_create_course(self):
        response = self.app.post('/api/courses', data=json.dumps({
            'name': 'Test Course',
            'course_id': 'CS301',
            'teacher': 'Prof. Brown'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'],'Student deleted successfully')

    def test_get_courses(self):
        response = self.app.get('/api/courses')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(len(data['courses']) == 2)

    def test_get_course(self):
        response = self.app.get('/api/courses/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Introduction to Computer Science')

    def test_update_course(self):
        response = self.app.put('/api/courses/1', data=json.dumps({
            'name': 'Updated Course',
            'course_id': 'CS101',
            'teacher': 'Dr. Brown'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Course updated successfully')

    def test_delete_course(self):
        response = self.app.delete('/api/courses/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Course deleted successfully')

    def test_register_student(self):
        response = self.app.post('/api/courses/1/register', data=json.dumps({
            'student_id': '1002'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Student registered successfully')

    def test_get_enrollments(self):
        response = self.app.get('/api/courses/2/students')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(len(data['enrollments']) == 2)

    def test_get_grades(self):
        response = self.app.get('/api/students/1/grades')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(len(data['grades']) == 2)

    def test_calculate_gpa(self):
        response = self.app.get('/api/students/1/gpa')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['gpa'], 3.875)

if __name__ == '__main__':
    unittest.main()

