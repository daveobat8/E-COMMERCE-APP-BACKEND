from models import db, User, Product, Category, Order, OrderItem, ShoppingCart, CartItem, Address, Payment, Review
import datetime
from app import app

with app.app_context():
    db.create_all()
    # Create categories
    categories = [
        Category(name='Electronics'),
        Category(name='Books'),
        Category(name='Clothing'),
        Category(name='Home & Garden'),
        Category(name='Toys & Games')
    ]
    
    db.session.bulk_save_objects(categories)
    db.session.commit()

    # Create users
    users = [
        User(username='john_doe', email='john@example.com', first_name='John', last_name='Doe', password='1234'),
        User(username='jane_smith', email='jane@example.com', first_name='Jane', last_name='Smith', password='1234', is_admin=True),
        User(username='mike_johnson', email='mike@example.com', first_name='Mike', last_name='Johnson', password='1234'),
        User(username='sara_connor', email='sara@example.com', first_name='Sara', last_name='Connor', password='1234'),
    ]
    
    db.session.bulk_save_objects(users)
    db.session.commit()

    # Create products
    products = [
        Product(name='Smartphone', description='Latest model smartphone with advanced features.', price=699.99, stock=50, image_url='http://example.com/smartphone.jpg', category_id=1),
        Product(name='Laptop', description='High performance laptop for gaming and productivity.', price=1199.99, stock=30, image_url='http://example.com/laptop.jpg', category_id=1),
        Product(name='Science Fiction Novel', description='An exciting journey through space.', price=19.99, stock=100, image_url='http://example.com/scifi_novel.jpg', category_id=2),
        Product(name='T-Shirt', description='Comfortable cotton t-shirt.', price=25.00, stock=200, image_url='http://example.com/tshirt.jpg', category_id=3),
        Product(name='Garden Tool Set', description='Essential tools for your gardening needs.', price=49.99, stock=75, image_url='http://example.com/garden_tools.jpg', category_id=4),
        Product(name='Puzzle', description='Fun and challenging puzzle for all ages.', price=15.00, stock=120, image_url='http://example.com/puzzle.jpg', category_id=5)
    ]

    db.session.bulk_save_objects(products)
    db.session.commit()

    # Create addresses
    addresses = [
        Address(user_id=1, street='123 Main St', city='New York', county='New York', country='USA'),
        Address(user_id=2, street='456 Park Ave', city='Los Angeles', county='Los Angeles', country='USA'),
        Address(user_id=3, street='789 Broadway', city='Chicago', county='Cook', country='USA'),
    ]

    db.session.bulk_save_objects(addresses)
    db.session.commit()

    # Create shopping carts
    shopping_carts = [
        ShoppingCart(user_id=1),
        ShoppingCart(user_id=2),
    ]

    db.session.bulk_save_objects(shopping_carts)
    db.session.commit()

    # Create cart items
    cart_items = [
        CartItem(cart_id=1, product_id=1, quantity=1),
        CartItem(cart_id=1, product_id=3, quantity=2),
        CartItem(cart_id=2, product_id=2, quantity=1),
    ]

    db.session.bulk_save_objects(cart_items)
    db.session.commit()

    # Create orders
    orders = [
        Order(user_id=1, total_amount=739.97, created_at=datetime.datetime.utcnow()),
        Order(user_id=2, total_amount=1199.99, created_at=datetime.datetime.utcnow()),
    ]

    db.session.bulk_save_objects(orders)
    db.session.commit()

    # Create order items
    order_items = [
        OrderItem(order_id=1, product_id=1, quantity=1),
        OrderItem(order_id=1, product_id=3, quantity=2),
        OrderItem(order_id=2, product_id=2, quantity=1),
    ]

    db.session.bulk_save_objects(order_items)
    db.session.commit()

    # Create payments
    payments = [
        Payment(order_id=1, amount=739.97, payment_method='credit card', payment_status='completed'),
        Payment(order_id=2, amount=1199.99, payment_method='PayPal', payment_status='completed'),
    ]

    db.session.bulk_save_objects(payments)
    db.session.commit()

    # Create reviews
    reviews = [
        Review(product_id=1, user_id=1, rating=5, product_review='Excellent smartphone, highly recommend!'),
        Review(product_id=2, user_id=2, rating=4, product_review='Great laptop but a bit pricey.'),
        Review(product_id=3, user_id=3, rating=5, product_review='Loved the science fiction novel, very engaging.'),
    ]

    db.session.bulk_save_objects(reviews)
    db.session.commit()


