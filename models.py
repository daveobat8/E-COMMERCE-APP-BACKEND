from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum

import datetime


db= SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id= db.Column(db.Integer, primary_key=True) 
    username= db.Column(db.String(80), unique=True, nullable=False)
    email= db.Column(db.String(120), unique=True, nullable=False)
    first_name= db.Column(db.String(20), nullable=False)
    last_name= db.Column(db.String(20), nullable=False)
    password= db.Column(db.String(50), nullable=False)
    is_admin= db.Column(db.Boolean, default=False)
    #one to many relationship between users and order
    orders= db.relationship('Order', backref= 'user', lazy=True)
    shopping_cart = db.relationship('ShoppingCart', backref='user', uselist=False, lazy=True)
    addresses= db.relationship('Address', backref= 'user', lazy=True)
    reviews = db.relationship('Review', backref='user', lazy=True)

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    order_items = db.relationship('OrderItem', backref='product', lazy=True)
    cart_items = db.relationship('CartItem', back_populates='product_item', lazy=True)
    reviews = db.relationship('Review', back_populates='product', lazy=True)


class Category(db.Model):
    __tablename__= 'categories'

    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    #one to many relationship between Category and its products
    products= db.relationship('Product', backref= 'category', lazy=True)

class Order(db.Model):
    __tablename__= 'orders'

    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id') ,nullable=False)
    total_amount= db.Column(db.Float, nullable=False)
    #Enum allows for a strict control over the option that can be used
    status = db.Column(Enum('pending', 'shipped', 'delivered', 'canceled', 'refunded', name='order_status'), default='pending')
    created_at= db.Column(db.DateTime)
    items= db.relationship('OrderItem', backref='order', lazy=True)
    payments = db.relationship('Payment', backref='order', lazy=True)

class OrderItem(db.Model):
    __tablename__= 'order_items'

    id= db.Column(db.Integer, primary_key=True)
    quantity= db.Column(db.Float, nullable=False)
    order_id= db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

class ShoppingCart(db.Model):
    __tablename__ = 'shopping_carts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('CartItem', back_populates='shopping_cart', lazy=True)


class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('shopping_carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    shopping_cart = db.relationship('ShoppingCart', back_populates='items')
    product_item = db.relationship('Product', back_populates='cart_items')


class Address(db.Model):
    __tablename__ = 'addresses'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(50), nullable=False)

class Payment(db.Model):
    __tablename__ = 'payments'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)  # e.g., credit card, PayPal
    payment_status = db.Column(db.String(20), default='pending')  # pending, completed, failed
    payment_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1 to 5 stars
    product_review = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    product = db.relationship('Product', back_populates='reviews')