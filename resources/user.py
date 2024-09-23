from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request




from models import db, User
from schemas import UserSchema, user_schema, users_schema

#user signup resource
class User_Signup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required= True, help='username is required')
    parser.add_argument('email', required= True, help='email is required')
    parser.add_argument('first_name', required= True, help='first_name is required')
    parser.add_argument('last_name', required= True, help='last_name is required')
    parser.add_argument('password', required= True, help='password is required')

    #endpoints
    def get(self):
        users= User.query.all()

        response= make_response(
            users_schema.dump(users), 
            200
        )

        return response
    

    def post(self):
        data= User_Signup.parser.parse_args()
        new_user= User(**data)

        #ensure that email and password are both input
        if not new_user.email or not new_user.password:
            return {'message': "Both email and password are required"}, 400
        
        #check if email is already registered
        if User.query.filter_by(email= new_user.email).first():
            return {'message':'User is already registered'}, 400
        
        db.session.add(new_user)
        db.session.commit()

        return {'messsage': 'User registered successfully'}, 201
    

