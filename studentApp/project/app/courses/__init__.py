from flask import Blueprint
from flask_restx import Api

from courses import api as course_api

bp = Blueprint('courses', __name__, url_prefix='/api/courses')
api = Api(bp, title='Courses API', version='1.0', description='API for managing courses and course students')

api.add_namespace(course_api)

