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
from resources.product import Product_list, Product_by_id
from resources.category import Category_list, Category_by_id
from resources.order import Order_list, Order_by_id
from resources.order_item import Order_item_list, Order_item_by_id
from resources.shopping_cart import ShoppingCart_list, ShoppingCart_by_id
from resources.cart_item import CartItem_list, CartItem_by_id
from resources.address import Address_list, Address_by_id
from resources.payment import Payment_list, Payment_by_id

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

api.add_resource(Product_list, '/products')
api.add_resource(Product_by_id, '/products/<int:id>')

api.add_resource(Category_list, '/category')
api.add_resource(Category_by_id, '/category/<int:id>')

api.add_resource(Order_list, '/orders')
api.add_resource(Order_by_id, '/orders/<int:id>')

api.add_resource(Order_item_list, 'order_items')
api.add_resource(Order_item_by_id, 'order_items/<int:id>')

api.add_resource(ShoppingCart_list, '/shoppingcarts')
api.add_resource(ShoppingCart_by_id, '/shoppingcarts/<int:id>')

api.add_resource(CartItem_list,'/cart_items')
api.add_resource(CartItem_by_id,'/cart_items/<int:id>')

api.add_resource(Address_list, '/addresses')
api.add_resource(Address_by_id, '/addresses/<int:id>')


api.add_resource(Payment_list, '/payments')
api.add_resource(Payment_by_id, '/payments/<int:id>')


if __name__ == '__main__':
    app.run(port=5555,debug=True)