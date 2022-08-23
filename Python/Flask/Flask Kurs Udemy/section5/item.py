import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price', type=float,
        required=True,
        help='set the item price'
    )

    @jwt_required()
    def get(self, name: str):
        item = self.find_item_by_name(name)
        if item:
            return item
        return {'message': 'Item does not exist'}, 404

    @staticmethod
    def find_item_by_name(name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"

        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {
                'id': row[0],
                'name': row[1],
                'price': row[2]
            }}

    @staticmethod
    def add_item_to_database(name, price):
        item = {'name': name, 'price': price}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (NULL, ?, ?)"
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()
        return item

    def post(self, name: str):
        if self.find_item_by_name(name):
            return {"message": "item already exists in database"}, 400

        data = Item.parser.parse_args()

        try:
            item = self.add_item_to_database(name, data['price'])
        except:
            return {"message": "An error occurred while adding item"}, 500
        return item, 201
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name = ?"

        cursor.execute(query, (name,))
        connection.commit()
        connection.close()

        return {'message': 'items were deleted successfully'}
    def put(self, name):
        data = Item.parser.parse_args()
        if self.find_item_by_name(name):
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "UPDATE items SET price=? WHERE name=?"
            cursor.execute(query, (data['price'], name))
            connection.commit()
            connection.close()
            return {'message': f"item {name} was updated"}
        else:
            try:
                item = self.add_item_to_database(name, data['price'])
            except:
                return {"message": "An error occurred while adding item"}, 500
            return {'message': 'item was successfully added'}

class Items(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'id': row[0], 'name': row[1], 'price': row[2]})

        connection.close()

        return {'items': items}, 200
