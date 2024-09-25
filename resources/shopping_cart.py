from flask_restful import Resource,  reqparse
from flask import jsonify, make_response, request


from models import ShoppingCart, db
from schemas import ShoppingCartSchema, shoppingcart_schema, shoppingcarts_schema


class ShoppingCart_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id', type=int, required=True, help="User ID is required")

    def get(self):
        shopping_carts= ShoppingCart.query.all()

        response= make_response(
            shoppingcarts_schema.dump(shopping_carts), 200
        )

        return response
    
    def post(self):
        data= ShoppingCart_list.parser.parse_args()
        new_shoppingcart= ShoppingCart(**data)

        db.session.add(new_shoppingcart)
        db.session.commit()

        response= make_response(
            shoppingcart_schema.dump(new_shoppingcart), 200
        )

        return response
    
class ShoppingCart_by_id(Resource):
    def get(self, id):
        shoppingcart= ShoppingCart.query.filter_by(id=id).first()

        if shoppingcart == None:
            response_body= {
                "error" : "shopping cart does not exist"
            }
            response= make_response(
                jsonify(response_body),404
            )

            return response
        else:
            response= make_response(
                shoppingcart_schema.dump(shoppingcart), 200
            )

            return response

    def patch(self, id):
        shoppingcart= ShoppingCart.query.filter_by(id=id).first()

        data= request.get_json()

        for attr,value in data.items():
            if hasattr(shoppingcart, attr):
                setattr(shoppingcart,attr,value)

        db.session.add(shoppingcart)
        db.session.commit()

        response= make_response(
            shoppingcart_schema.dump(shoppingcart), 201
        )

        return response
    

    def delete(self, id):
        shoppingcart= ShoppingCart.query.filter_by(id=id).first()

        db.session.delete(shoppingcart)
        db.session.commit()

        response_body= {
            "delete_successful": True,
            "message": "Shopping cart data deleted successfully"
        }

        response= make_response(
            jsonify(response_body), 200
        )

        return response