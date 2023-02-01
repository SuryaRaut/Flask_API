import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db_V1 import stores
from schemas import StoreSchema, StoreUpdateSchema

blp = Blueprint( 'stores', __name__, description="Opeations on stores" )

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

    @blp.arguments( StoreUpdateSchema )
    def put( self, put_store_data, store_id ):

        if( not stores.get( store_id ) ):
            abort( 404, message= f"Item not Found having store_id = { store_id }" )
        
        stores[ store_id ]["store_name"] = put_store_data["store_name"]

        return stores[ store_id ], 202
    
@blp.route('/addStore')
class AddStore(MethodView):

    @blp.arguments( StoreSchema )
    def post(self, store_data):

        store_id = uuid.uuid4().hex
        store_data['store_id'] = store_id
        store_data['items'] = []
        print( f"store_data = { store_data }" )

        stores[store_id] = store_data

        return store_data, 201

@blp.route("/stores")
class Stores( MethodView ):
    def get( self ):
        return stores, 200