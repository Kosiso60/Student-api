from flask import Blueprint
from flask_restx import Api

from students import api as student_api

bp = Blueprint('students', __name__, url_prefix='/api/students')
api = Api(bp, title='Students API', version='1.0', description='API for managing students')

api.add_namespace(student_api)

