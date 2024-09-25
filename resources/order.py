from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request


from models import db, Order
from schemas import OrderSchema, order_schema, orders_schema


class Order_list(Resource):
    parser= reqparse.RequestParser()
    parser.add_argument('user_id', type=int, required= True, help="User ID is required")
    parser.add_argument('total_amount', type=float, required=True, help="Total amount is required.")
    parser.add_argument('status', type=str, choices=['pending', 'shipped', 'delivered', 'canceled', 'refunded'], default='pending')
    parser.add_argument('created_at', type=str, required=False, help="Created date in YYYY-MM-DD format.")
    parser.add_argument('items', type=dict, action='append', help="Items in the order.")

    def get(self):
        orders= Order.query.all()

        response= make_response(
            orders_schema.dump(orders), 200
        )

        return response
    
    def post(self):
        data= Order_list.parser.parse_args()

        new_order= Order(**data)

        db.session.add(new_order)
        db.session.commit()

        response= make_response(
            order_schema.dump(new_order), 200
        )

        return response
    

class Order_by_id(Resource):
    def get(self, id):
        order= Order.query.filter_by(id=id).first()

        if order == None:
            response_body= {
                "error" : "order does not exist"
            }
            response= make_response(
                jsonify(response_body), 404
            )
            return response
        else:
            response= make_response(
                order_schema.dump(order), 200
            )

            return response
        
    def patch(self, id):
        order= Order.query.filter_by(id=id).first()

        data= request.get_json()

        for attr, value in data.items():
            if hasattr(order, attr):
                setattr(order, attr, value)

        db.session.add(order)
        db.session.commit()

        response= make_response(
            order_schema.dump(order), 200
        )
        return response
    
    def delete(self ,id):
        order= Order.query.filter_by(id=id).first()

        db.session.delete(order)
        db.session.commit()

        response_body= {
            "delete_successful": True,
            "message": "Product data deleted successfully"
        }

        response= make_response(
            jsonify(response_body), 200
        )

        return response