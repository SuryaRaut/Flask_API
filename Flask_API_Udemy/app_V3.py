import uuid
from flask import Flask, request
from db_V1 import *
from flask_smorest import abort

app = Flask(__name__)

@app.get( '/' ) # http://127.0.0.1:5000/
def welcomeNote():
    return { "Welcome" : "Welcome to Our Grocery App" }, 200
    # return "Hello"

@app.post( '/addStore' ) # http://127.0.0.1:5000/addStore
def create_store():
    store_data = request.get_json()
    if( "store_name" not in store_data ):
        abort( 404, message= f"API does not have required parameters" )

    store_id = uuid.uuid4().hex
    store_data['store_id'] = store_id
    store_data['items'] = []
    print( f"store_data = { store_data }" )

    stores[store_id] = store_data

    return store_data, 201

@app.get( '/stores' ) # http://127.0.0.1:5000/stores
def getallstores():
    return stores, 200

@app.get( '/store/<string:store_id>' ) # http://127.0.0.1:5000/store/store_id
def getStore(store_id):
    try:
        return stores[store_id], 200
    except KeyError as e:
        # return { "Error" : f"Store not Found, Exception = {e}" }, 404
        abort( 404, message= f"Store not Found, Exception = {e}" )

@app.delete( '/store/<string:store_id>' ) # http://127.0.0.1:5000/store/store_id
def deletestore(store_id):
    try:
        op = stores.pop( store_id )
        return op, 202
    except KeyError as e:
        abort( 404, message= f"Store not Found having store_id = { store_id }" )

@app.put( '/store/<string:store_id>' ) # http://127.0.0.1:5000/item/item_id
def putStore(store_id):
    put_store_data = request.get_json()

    if( store_id not in stores ):
        abort( 404, message= f"Item not Found having store_id = { store_id }" )
    
    if( "store_name" not in put_store_data ):
        abort( 404, message= f"API does not have required parameters" )

    stores[ store_id ]["store_name"] = put_store_data["store_name"]

    return stores[ store_id ], 202

@app.post( '/addItem' ) # http://127.0.0.1:5000/addItem
def addItem():
    item_data = request.get_json()
    print( f"item_data = { item_data }")

    if( ("store_id" not in item_data)
        and ("item_name" not in item_data)
        and ("item_price" not in item_data) ):
        abort( 404, message= f"API does not have required parameters" )

    if( item_data["store_id"] not in stores ):
        # return { "Error" : f"Store not found having store_id : { item_data['store_id'] }" }
        abort( 404, message= f"Store not found having store_id : { item_data['store_id'] }" )
    
    
    for each_item in items.values():
        if( ( each_item["store_id"] == item_data["store_id"] )
        and ( each_item["item_name"] == item_data["item_name"] ) ):
            abort( 404, message= f"Duplicate Item present in store_id : { item_data['store_id'] }" )
    
    item_id = uuid.uuid4().hex
    item_data["item_id"] = item_id

    items[item_id] = item_data
    
    return item_data, 201

@app.get( '/items' ) # http://127.0.0.1:5000/items
def getallitems():
    return items, 200

@app.get( '/item/<string:item_id>' ) # http://127.0.0.1:5000/item/item_id
def getitem(item_id):
    try:
        return items[item_id], 200
    except KeyError as e:
        # return { "Error" : f"Item not Found, Exception = {e}" }, 404
        abort( 404, message= f"Item not Found, Exception = {e}" )

@app.delete( '/item/<string:item_id>' ) # http://127.0.0.1:5000/item/item_id
def deleteitem(item_id):
    try:
        op = items.pop( item_id )
        return op, 202
    except KeyError as e:
        abort( 404, message= f"Item not Found having item_id = { item_id }" )

@app.put( '/item/<string:item_id>' ) # http://127.0.0.1:5000/item/item_id
def putItem(item_id):
    put_item_data = request.get_json()

    if( item_id not in items ):
        abort( 404, message= f"Item not Found having item_id = { item_id }" )
    
    if( ("item_name" not in put_item_data)  and ("item_price" not in put_item_data) ):
        abort( 404, message= f"API does not have required parameters" )

    items[ item_id ]["item_name"] = put_item_data["item_name"]
    items[ item_id ]["item_price"] = put_item_data["item_price"]

    if("store_id" in put_item_data):
        items[ item_id ]["store_id"] = put_item_data["store_id"]
        
    return items[ item_id ], 202

app.run()