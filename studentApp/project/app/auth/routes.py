from flask import request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.auth.models import User
from app import api

auth_ns = api.namespace('auth', description='Authentication operations')

@auth_ns.route('/login')
class LoginResource(Resource):
    def post(self):
        data = request.json
        user = User.query.filter_by(username=data['username']).first()

        if not user or not user.check_password(data['password']):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=user.username)
        return {'access_token': access_token}, 200

@auth_ns.route('/protected')
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {'logged_in_as': current_user}, 200
