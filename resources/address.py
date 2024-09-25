from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request


from models import Address, db
from schemas import AddressSchema, address_schema, addresses_schema

class Address_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id', type=int, required=True, help="User ID is required")
    parser.add_argument('street', type=str, required=True, help="Street is required")
    parser.add_argument('city', type=str, required=True, help="City is required")
    parser.add_argument('county', type=str, required=True, help="County is required")
    parser.add_argument('country', type=str, required=True, help="Country is required")

    def get(self):
        addresses= Address.query.all()

        response= make_response(
            addresses_schema.dump(addresses), 200
        )

        return response
    
    def post(self):
        data= Adress_list.parser.parse_args()
        new_address= Address(**data)

        db.session.add(new_address)
        db.session.commit()

        response= make_response(
            address_schema.dump(new_address), 200
        )

        return response
    

class Address_by_id(Resource):
    def get(self, id):
        address= Address.query.filter_by(id=id).first()

        if address == None:
            response_body= {
                "error" : "address does not exist"
            }
            response= make_response(
                jsonify(response_body),404
            )

            return response
        else:
            response= make_response(
                address_schema.dump(address), 200
            )

            return response
        

    def patch(self, id):
        address= Address.query.filter_by(id=id).first()

        data= request.get_json()

        for attr,value in data.items():
            if hasattr(address, attr):
                setattr(address,attr,value)

        db.session.add(address)
        db.session.commit()

        response= make_response(
            address_schema.dump(address), 201
        )

        return response
    
    def delete(self, id):
        address= Address.query.filter_by(id=id).first()

        db.session.delete(address)
        db.session.commit()

        response_body= {
            "delete_successful": True,
            "message": "address data deleted successfully"
        }

        response= make_response(
            jsonify(response_body), 200
        )

        return response