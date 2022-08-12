from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'MyFirstStore',
        'items': [
            {
                'name': 'My item',
                'price': 9.99,
            },
        ],
    },
]

def error(object:str) -> str:
    return f"i cant find this {object}"
#post to recive data

#get to send data back only

#post /store data: {name:}
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify({"added_store": new_store})
#get /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"store": store})
    return jsonify({"message": error("store")})
#get /store
@app.route("/store")
def get_stores():
    return jsonify({'stores': stores})
#post /store/<string: name>/item
@app.route("/store/<string:name>/items", methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({'added_item': new_item})
    return jsonify({"message": error("store")})
#GET /store/<string:name>/item
@app.route("/store/<string:name>/items")
def render_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items": store['items']})
    return jsonify({"message": error("store")})

app.run(port=1234)