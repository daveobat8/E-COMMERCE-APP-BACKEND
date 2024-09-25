from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token
from flask_bcrypt import Bcrypt,generate_password_hash



from models import db, User
from schemas import UserSchema, user_schema, users_schema

bcrypt = Bcrypt()

jwt = JWTManager()
user_schema = UserSchema()

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
        
        new_user.password = generate_password_hash(new_user.password).decode('utf-8')
        
        db.session.add(new_user)
        db.session.commit()

        return {'messsage': 'User registered successfully'}, 201
    
#user login resource
class User_Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', required=True, help="Email address is required")
    parser.add_argument('password', required=True, help="Password is required")

    def post(self):
        data= User_Login.parser.parse_args()

        user= User.query.filter_by(email= data['email']).first()

        if user:
            password_is_correct= user.check_password(data['password'])
            if password_is_correct:
                user_json= user_schema.dump(user)
                access_token= create_access_token(identity=user_json['id'])
                refresh_token= create_refresh_token(identity=user_json['id'])

                return {
                    "message":"Login successful",
                    "status":"success",
                    "access_token":access_token,
                    "refresh_token":refresh_token,
                    "user": user_json
                }, 200
            else:
                return {"message":"Invalid email or password"}, 401
            
        else:
            return {"message":"User not found"}, 404


class User_list(Resource):

    def get(self):
        users= User.query.all()

        response= make_response(
            users_schema.dump(users), 200
        )

        return response
    

class User_by_id(Resource):

    def get(self, id):
        user= User.query.filter_by(id=id).first()

        if user == None:
            response_body = {
                "error" : "user does not exist"
            }
            response = make_response(
                jsonify(response_body),
                404)
            
            return response
        
        else:
            response = make_response(
                user_schema.dump(user),
                200
            )
            return response
        
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(user, attr, request.get_json().get(attr))

        db.session.add(user)
        db.session.commit()

        response= make_response(
            user_schema.dump(user),
            201
        )

        return response
    
    def delete(self,id):
        user = User.query.filter_by(id=id).first()
        
        db.session.delete(user)
        db.session.commit()


        response_body = {
            "delete_successful": True,
            "message": "user data deleted successfully"
        }

        response = make_response(
            jsonify(response_body),
            200
        )

        return response