from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request


from models import CartItem, db
from schemas import CartItemSchema, cartitem_schema, cartitems_schema

class Cart_Item_list(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('cart_id', type=int, required=True, help="Cart ID is required")
    parser.add_argument('product_id', type=int, required=True, help="Product ID is required")
    parser.add_argument('quantity', type=int, required=True, help="Quantity is required")

    def get(self):
        cart_items= CartItem.query.all()

        response= make_response(
            cartitems_schema.dump(cart_items), 200
        )

        return response
    
    def post(self):
        data= Cart_Item_list.parser.parse_args()
        new_cartitem= CartItem(**data)

        db.session.add(new_cartitem)
        db.session.commit()

        response= make_response(
            cartitem_schema.dump(new_cartitem), 200
        )

        return response
    

class CartItem_by_id(Resource):
    def get(self, id):
        cart_item= CartItem.query.filter_by(id=id).first()

        if cart_item == None:
            response_body= {
                "error" : "cart_item does not exist"
            }
            response= make_response(
                jsonify(response_body),404
            )

            return response
        else:
            response= make_response(
                cartitem_schema.dump(cart_item), 200
            )

            return response
        
    def patch(self, id):
        cart_item= CartItem.query.filter_by(id=id).first()

        data= request.get_json()

        for attr,value in data.items():
            if hasattr(cart_item, attr):
                setattr(cart_item,attr,value)

        db.session.add(cart_item)
        db.session.commit()

        response= make_response(
            cartitem_schema.dump(cart_item), 201
        )

        return response
    
    def delete(self, id):
        cart_item= CartItem.query.filter_by(id=id).first()

        db.session.delete(cart_item)
        db.session.commit()

        response_body= {
            "delete_successful": True,
            "message": "cart_item data deleted successfully"
        }

        response= make_response(
            jsonify(response_body), 200
        )

        return response