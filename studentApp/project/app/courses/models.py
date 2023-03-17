from app import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(100), nullable=False)
    students = db.relationship('CourseStudent', backref='course', lazy=True)

class CourseStudent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.Float)

    @property
    def gpa(self):
        if self.grade is None:
            return None
        elif self.grade >= 90:
            return 4.0
        elif self.grade >= 80:
            return 3.0
        elif self.grade >= 70:
            return 2.0
        elif self.grade >= 60:
            return 1.0
        else:
            return 0.0

    @classmethod
    def get_by_course_and_student(cls, course_id, student_id):
        return cls.query.filter_by(course_id=course_id, student_id=student_id).first()

    @classmethod
    def get_all_by_course(cls, course_id):
        return cls.query.filter_by(course_id=course_id).all()
