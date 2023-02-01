from flask import Flask, request

app = Flask(__name__) # Flask( '__main__' )

stores_list = [
    {   # Store 1 Data Start
        "store_name" : "Store 1"
        , "items" : [
            {
                "item_name" : "Item 1"
                , "item_name" : 15.99
            }
        ]
    }   # Store 1 Data End
]

# http://127.0.0.1:5001/

@app.get( '/' ) # http://127.0.0.1:5000/
def welcomeNote():
    return { "Welcome" : "Welcome to Our Grocery App" }

@app.post( '/addStore' ) # http://127.0.0.1:5000/addStore
def create_store():
    request_data = request.get_json()
    print( f"create_store() : request_data = {request_data}\n" )

    new_store = {"store_name" : request_data["store_name"], "items" : [] }
    print( f"create_store() : new_store = {new_store}\n" )

    stores_list.append( new_store )

    # return new_store
    return new_store, 201

@app.get( '/stores' ) # http://127.0.0.1:5000/stores
def get_stores():
    return { "Stores" : stores_list }, 200
    # return str( stores )

@app.get( '/store/<string:store>' ) # http://127.0.0.1:5000/store/store_name
def getStore(store):
    print( f"getStore() : store = { store }\n" )
    try:
        selected_store = list( filter( lambda i : i['store_name'] == store , stores_list ) )[0]

        return selected_store, 200
    except Exception as e:
        return { "Error" : f"No Data Found, Exception = {e}" }, 404

@app.post( '/store/<string:store>/addItem' ) # http://127.0.0.1:5000/store/store_name/addItem
def addItem(store):
    request_data = request.get_json()
    print( f"addItem() : request_data = { request_data }\n" )

    item_data = { "item_name" : request_data["item_name"]
                , "item_price" : request_data["item_price"]
                 }

    try:
        selected_store = list( filter( lambda i : i['store_name'] == store , stores_list ) )[0] # [][0]
        print( f"addItem() : selected_store = { selected_store }\n" )

        selected_store["items"].append( item_data )

        return selected_store, 201

    except Exception as e:
        return { "Error" : f"No Data Found, Exception = {e}" }, 404

app.run()
