from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request



from models import db, Payment
from schemas import PaymentSchema, payment_schema, payments_schema

class Payment_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('order_id', type=int, required=True, help="Order ID is required")
    parser.add_argument('amount', type=float, required=True, help="Payment amount is required")
    parser.add_argument('payment_method', type=str, required=True, help="Payment method is required")
    parser.add_argument('payment_status', type=str, choices=('pending', 'completed', 'failed'), help="Invalid payment status")

    def get(self):
        payments= Payment.query.all()

        response= make_response(
            payments_schema.dump(payments), 200
        )

        return response
    
    def post(self):
        data= Payment_list.parser.parse_args()
        new_payment= Payment(**data)

        db.session.add(new_payment)
        db.session.commit()

        response= make_response(
            payment_schema.dump(new_payment), 200
        )

        return response
    
class Payment_by_id(Resource):
    def get(self, id):
        payment= Payment.query.filter_by(id=id).first()

        if payment == None:
            response_body= {
                "error" : "payment does not exist"
            }
            response= make_response(
                jsonify(response_body),404
            )

            return response
        else:
            response= make_response(
                payment_schema.dump(payment), 200
            )

            return response
        
    def patch(self, id):
        payment= Payment.query.filter_by(id=id).first()

        data= request.get_json()

        for attr,value in data.items():
            if hasattr(payment, attr):
                setattr(payment,attr,value)

        db.session.add(payment)
        db.session.commit()

        response= make_response(
            payment_schema.dump(payment), 201
        )

        return response
    
    def delete(self, id):
        payment= Payment.query.filter_by(id=id).first()

        db.session.delete(payment)
        db.session.commit()

        response_body= {
            "delete_successful": True,
            "message": "payment data deleted successfully"
        }

        response= make_response(
            jsonify(response_body), 200
        )

        return response