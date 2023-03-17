from app import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@property
def gpa(self):
    total_credits = 0
    total_points = 0
    for enrollment in self.enrollments:
        if enrollment.grade >= 90:
            points = 4.0
        elif enrollment.grade >= 80:
            points = 3.0
        elif enrollment.grade >= 70:
            points = 2.0
        elif enrollment.grade >= 60:
            points = 1.0
        else:
            points = 0.0
        total_credits += enrollment.course.credits
        total_points += points * enrollment.course.credits
    return total_points / total_credits if total_credits > 0 else 0.0
