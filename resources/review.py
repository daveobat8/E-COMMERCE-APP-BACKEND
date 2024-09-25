from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request



from models import db, Review
from schemas import ReviewSchema, review_schema, reviews_schema

class Review_list(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('product_id', type=int, required=True, help="Product ID is required")
    parser.add_argument('user_id', type=int, required=True, help="User ID is required")
    parser.add_argument('rating', type=int, required=True, help="Rating is required and should be between 1 and 5")
    parser.add_argument('product_review', type=str, required=False, help="Review content is optional")

    def get(self):
        reviews= Review.query.all()

        response= make_response(
            reviews_schema.dump(reviews), 200
        )

        return response
    
    def post(self):
        data= Review_list.parser.parse_args()
        new_review= Review(**data)

        db.session.add(new_review)
        db.session.commit()

        response= make_response(
            review_schema.dump(new_review), 200
        )

        return response
    
class Review_by_id(Resource):
    def get(self, id):
        review=  Review.query.filter_by(id=id).first()

        if review == None:
            response_body= {
                "error" : "review does not exist"
            }
            response= make_response(
                jsonify(response_body),404
            )

            return response
        else:
            response= make_response(
                review_schema.dump(review), 200
            )

            return response
        
    def patch(self, id):
        review=  Review.query.filter_by(id=id).first()

        data= request.get_json()

        for attr,value in data.items():
            if hasattr(review, attr):
                setattr(review,attr,value)

        db.session.add(review)
        db.session.commit()

        response= make_response(
            review_schema.dump(review), 201
        )

        return response

    def delete(self, id):
        review=  Review.query.filter_by(id=id).first()

        db.session.delete(review)
        db.session.commit()

        response_body= {
            "delete_successful": True,
            "message": "review data deleted successfully"
        }

        response= make_response(
            jsonify(response_body), 200
        )

        return response