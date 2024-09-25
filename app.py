from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager
from datetime import timedelta


from schemas import ma
from models import db

from resources.user import bcrypt,jwt, User_Signup, User_Login, User_by_id, User_list

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///e_commerce.db'
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

migrate =  Migrate(app, db)

db.init_app(app)
ma.init_app(app)


api=Api(app)

bcrypt.init_app(app)
jwt.init_app(app)


@app.route("/")
def index():
    return "message:" "your app is running"
    



api.add_resource(User_Signup, '/signup')
api.add_resource(User_Login, '/login')


if __name__ == '__main__':
    app.run(port=5555,debug=True)