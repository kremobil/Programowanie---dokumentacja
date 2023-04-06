import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema, ItemDeleteSchema

blueprint = Blueprint('items', __name__, description='Items operations')


@blueprint.route('/item/<string:item_id>')
class ItemById(MethodView):
    @blueprint.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            return abort(404, "Item not found")


    @blueprint.response(201, ItemDeleteSchema)
    def delete(self, item_id):
        try:
            item = items[item_id]
            del (items[item_id])
            return {"item": item, "message": "Item deleted"}
        except KeyError:
            return abort(404, "Item not found")

    @blueprint.arguments(ItemUpdateSchema)
    @blueprint.response(201, ItemSchema)
    def put(self, item_data, item_id):
        if item_id not in items:
            return abort(404, "Item not found")

        item = items[item_id]
        if "store_id" in item_data:
            if item_data["store_id"] not in stores:
                return abort(404, "Store not found")

        for key in item_data.keys():
            item[key] = item_data[key]
        return item


@blueprint.route('/items')
class Items(MethodView):
    @blueprint.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()


@blueprint.route('/item')
class Item(MethodView):
    @blueprint.arguments(ItemSchema)
    @blueprint.response(201, ItemSchema)
    def post(self, item_data):
        # checking is item already exists
        for item in items.values():
            if item["name"] == item_data["name"] and item["store_id"] == item_data:
                abort(400, message="Item already exists")

        # checking if store exists
        if item_data["store_id"] not in stores:
            return abort(404, "Store not found")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item
