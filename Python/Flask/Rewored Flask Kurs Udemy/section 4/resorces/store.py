import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema, StoreDeleteSchema

blueprint = Blueprint('stores', __name__, description='Stores operations')


@blueprint.route('/store/<string:store_id>')
class StoreById(MethodView):
    @blueprint.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            return abort(404, "Store not found")


    @blueprint.response(200, StoreDeleteSchema)
    def delete(self, store_id):
        try:
            store = stores[store_id]
            del (stores[store_id])
            return {"store": store, "message": "Store deleted"}
        except KeyError:
            return abort(404, "Store not found")

    @blueprint.arguments(StoreSchema)
    @blueprint.response(201, StoreSchema)
    def put(self, store_data, store_id):
        if store_id not in stores:
            return abort(404, "Store not found")

        store = stores[store_id]
        store["store_name"] = store_data["store_name"]
        return store


@blueprint.route('/stores')
class Stores(MethodView):
    @blueprint.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values()


@blueprint.route('/store/<string:store_name>')
class StoreByName(MethodView):
    @blueprint.response(201, StoreSchema)
    def post(self, store_name):
        for store in stores.values():
            if store["store_name"] == store_name:
                abort(400, message="Store already exists")

        store_id = uuid.uuid4().hex
        store = {"store_name": store_name, "id": store_id}
        stores[store_id] = store
        return store
