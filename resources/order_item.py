from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request


from models import OrderItem, db
from schemas import OrderItemSchema, order_item_schema, order_items_schema

class Order_item_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('quantity', type=float, required=True, help="Quantity is required")
    parser.add_argument('order_id', type=int, required=True, help="Order ID is required")
    parser.add_argument('product_id', type=int, required=True, help="Product ID is required")

    def get(self):
        order_items= OrderItem.query.all()

        response= make_response(
            order_items_schema.dump(order_items), 200
        )

        return response
    
    def post(self):
        data= Order_item_list.parser.parse_args()

        new_order_item= OrderItem(**data)

        db.session.add(new_order_item)
        db.session.commit()

        response= make_response(
            order_items_schema.dump(new_order_item), 200
        )

        return response


class Order_item_by_id(Resource):
    def get(self, id):
        order_item= OrderItem.query.filter_by(id=id).first()

        if order_item == None:
            response_body= {
                "error": "Order item does not exist"
            }
            response= make_response(
                jsonify(response_body), 404
            )
            return response
        else:
            response= make_response(
                order_item_schema.dump(order_item), 200
            )
            return response    
        

    def patch(self, id):
        order_item= OrderItem.query.filter_by(id=id).first()

        data= request.get_json()

        for attr,value in data.items():
            if hasattr(order_item, attr):
                setattr(order_item,attr,value)

        db.session.add(order_item)
        db.session.commit()

        response= make_response(
            order_item_schema.dump(order_item), 201
        )

        return response
    
    def delete(self, id):
        order_item= OrderItem.query.filter_by(id=id).first()

        db.session.delete(order_item)
        db.session.commit()

        response_body= {
            "delete_successful": True,
            "message": "Product data deleted successfully"
        }

        response= make_response(
            jsonify(response_body), 200
        )

        return response