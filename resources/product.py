from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request



from models import db, Product
from schemas import ProductSchema, product_schema, products_schema

class Product_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required= True, help= "name is required")
    parser.add_argument('description', required= True, help= "description is required")
    parser.add_argument('price', required= True, help= "price is required")
    parser.add_argument('stock', required= True, help= "stock is required")
    parser.add_argument('image_url', required= True, help= "image_url is required")
    parser.add_argument('category_id', required= True, help= "category_id is required")

    #requests
    def get(self):
        products= Product.query.all()

        response= make_response(
            products_schema.dump(products), 200
        )

        return response
    
    def post(self):
        data= Product_list.parser.parse_args()
        new_product= Product(**data)

        db.session.add(new_product)
        db.session.commit()

        response= make_response(
            product_schema.dump(new_product), 200
        )

        return response


class Product_by_id(Resource):
    #requests
    def get(self, id):
        #query the db and return one product by its ID
        product= Product.query.filter_by(id=id).first()

        #check if product exists
        if product == None:
            response_body= {
                "error" : "product does not exist"
            }
            response= make_response(
                jsonify(response_body),404
            )

            return response
        else:
            response= make_response(
                product_schema.dump(product), 200
            )

            return response
        
    def patch(self, id):
        #query db and return a single product
        product= Product.query.filter_by(id=id).first()

        data= request.get_json()

        for attr,value in data.items():
            if hasattr(product, attr):
                setattr(product,attr,value)

        db.session.add(product)
        db.session.commit()

        response= make_response(
            product_schema.dump(product), 201
        )

        return response
    
    def delete(self, id):
        product= Product.query.filter_by(id=id).first()

        db.session.delete(product)
        db.session.commit()

        response_body= {
            "delete_successful": True,
            "message": "Product data deleted successfully"
        }

        response= make_response(
            jsonify(response_body), 200
        )

        return response

