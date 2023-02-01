import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db_V1 import stores

blp = Blueprint( 'stores', __name__, description="Opeations on stores" )
# The Blueprint arguments are the same as the Flask Blueprint, with an added optional description keyword argument:
# "stores" is the name of the blueprint. This will be shown in the documentation

@blp.route('/store/<string:store_id>')
class Store( MethodView ):
    def get( self, store_id ):
        try:
            return stores[store_id], 200
        except KeyError as e:
            # return { "Error" : f"Store not Found, Exception = {e}" }, 404
            abort( 404, message= f"Store not Found, Exception = {e}" )

    def delete( self, store_id ):
        try:
            op = stores.pop( store_id )
            return op, 202
        except KeyError as e:
            abort( 404, message= f"Store not Found having store_id = { store_id }" )

    def put( self, store_id ):
        put_store_data = request.get_json()

        if( not stores.get( store_id ) ):
            abort( 404, message= f"Item not Found having store_id = { store_id }" )
        
        if( "store_name" not in put_store_data ):
            abort( 404, message= f"API does not have required parameters" )

        stores[ store_id ]["store_name"] = put_store_data["store_name"]

        return stores[ store_id ], 202
    
@blp.route('/addStore')
class AddStore(MethodView):
    def post(self):
        store_data = request.get_json()
        if( ("store_name" not in store_data) and ("store_type" not in store_data) ):
            abort( 404, message= f"API does not have required parameters" )

        store_id = uuid.uuid4().hex
        store_data['store_id'] = store_id
        store_data['items'] = []
        print( f"store_data = { store_data }" )

        stores[store_id] = store_data

        return store_data, 201

@blp.route("/stores")
class Stores( MethodView ):
    def get( self ):
        # return stores, 200
        return stores, 200