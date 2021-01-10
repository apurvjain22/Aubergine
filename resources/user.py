from flask import jsonify
from flask_restful import Resource, reqparse
from A2.models.user import UserModel


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('firstname', type=str, required=True, help="This field cannot be empty")
    parser.add_argument('lastname', type=str, required=True, help="This field cannot be empty")
    parser.add_argument('password', type=str, required=True, help="This field cannot be empty")
    parser.add_argument('email', type=str, required=True, help="This field cannot be empty")
    parser.add_argument('country', type=str, required=True, help="This field cannot be empty")

    def post(self):
        data = UserResource.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {'message': 'A user with that email is already exists'}, 400

        user = UserModel(data['firstname'], data['lastname'], data['password'], data['email'], data['country'])
        user.save_to_db()

        return {'message': 'User created successfully'}, 201


class UsersList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}
