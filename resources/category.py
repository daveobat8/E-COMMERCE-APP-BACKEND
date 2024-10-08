from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request


from models import db, Category
from schemas import CategorySchema, categories_schema, category_schema

class Category_list(Resource):
    parser= reqparse.RequestParser()
    parser.add_argument('name', required= True, help="name is required")

    def get(self):
        categories = Category.query.all()

        # For each category, we add a field for the product count
        result = categories_schema.dump(categories)

        for category in result:
            category['product_count'] = len(category['products'])  # Add product count

        response = make_response(result, 200)
        return response
    
    def post(self):
        data= Category_list.parser.parse_args()
        new_category= Category(**data)

        db.session.add(new_category)
        db.session.commit()

        response= make_response(
            category_schema.dump(new_category), 200
        )

        return response
    

class Category_by_id(Resource):
    def get(self, id):
        category = Category.query.filter_by(id=id).first()

        if category is None:
            response_body = {
                "error": "category does not exist"
            }
            response = make_response(
                jsonify(response_body), 404
            )
            return response
        else:
            result = category_schema.dump(category)
            result['product_count'] = len(result['products'])  # Add product count

            response = make_response(result, 200)
            return response
        
    def patch(self, id):
        category= Category.query.filter_by(id=id).first()

        data= request.get_json()

        for attr,value in data.items():
            if hasattr(category, attr):
                setattr(category,attr,value)

        db.session.add(category)
        db.session.commit()

        response= make_response(
            category_schema.dump(category), 201
        )

        return response
    
    def delete(self, id):
        category= Category.query.filter_by(id=id).first()

        db.session.delete(category)
        db.session.commit()

        response_body= {
            "delete_successful": True,
            "message": "Category data deleted successfully"
        }

        response= make_response(
            jsonify(response_body), 200
        )

        return response