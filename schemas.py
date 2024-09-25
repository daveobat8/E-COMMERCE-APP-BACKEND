from models import User, Product, Order, OrderItem, ShoppingCart, CartItem, Category, Address, Review, Payment
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema  # type: ignore


ma= Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= User
        load_instance= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("user_login", values=dict(id="<id>")),
            "collection": ma.URLFor("user_login"),
        }
    )

user_schema= UserSchema()
users_schema= UserSchema(many=True)

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Product
        include_fk= True
        load_instance= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("product_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("product_list"),
        }
    )

product_schema= ProductSchema()
products_schema= ProductSchema(many=True)

class OrderItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= OrderItem
        include_fk= True
        load_instance= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("order_item_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("order_item_list"),
        }
    )

order_item_schema= OrderItemSchema()
order_items_schema= OrderItemSchema(many= True)

class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Order
        include_fk= True
        load_instance= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("order_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("order_list"),
        }
    )

order_schema= OrderSchema()
orders_schema= OrderSchema(many= True)

class ShoppingCartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= ShoppingCart
        include_fk= True
        load_instance= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("shopping_cart_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("shopping_cart_list"),
        }
    )

shoppingcart_schema= ShoppingCartSchema()
shoppingcarts_schema= ShoppingCartSchema(many= True)

class CartItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= CartItem
        load_instance= True
        include_fk= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("cart_item_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("cart_item_list"),
        }
    )

cartitem_schema= CartItemSchema()
cartitems_schema= CartItemSchema(many= True)


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Category
        load_instance= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("category_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("category_list"),
        }
    )

category_schema= CategorySchema()
categories_schema= CategorySchema(many= True)

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Review
        load_instance= True
        include_fk= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("review_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("review_list"),
        }
    )

class PaymentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Payment
        load_instance= True
        include_fk= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("payment_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("payment_list"),
        }
    )

class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Address
        load_instance= True
        include_fk= True

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("address_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("address_list"),
        }
    )