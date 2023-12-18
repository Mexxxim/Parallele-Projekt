from flask import request
from flask_restful import Resource, Api
from models import db, Item  # Adjust import based on your actual models

api = Api()

class ItemResource(Resource):
    def post(self):
        data = request.get_json()

        # Assuming 'name' and 'description' are fields for your Item model
        name = data.get('name')
        description = data.get('quantity')

        if not name or not description:
            return {'message': 'Both name and quantity are required'}, 400

        new_item = Item(name=name, description=description)

        db.session.add(new_item)
        db.session.commit()

        return {'message': 'Item added successfully', 'item_id': new_item.id}, 201

api.add_resource(ItemResource, '/items')
