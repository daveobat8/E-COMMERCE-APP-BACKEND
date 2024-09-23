from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse

from schemas import ma
from models import db
from resources.user import User_Signup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///e_commerce.db'

migrate =  Migrate(app, db)

db.init_app(app)
ma.init_app(app)

api=Api(app)




@app.route("/")
def index():
    return "message:" "your app is running"
    



api.add_resource(User_Signup, '/signup')


if __name__ == '__main__':
    app.run(port=5555,debug=True)