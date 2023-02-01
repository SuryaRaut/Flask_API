import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db_V1 import items, stores
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint( 'items', __name__, description="Opeations on items" )

@blp.route('/item/<string:item_id>')
class Item( MethodView ):
    def get( self, item_id ):
        try:
            return items[item_id], 200
        except KeyError as e:
            # return { "Error" : f"Item not Found, Exception = {e}" }, 404
            abort( 404, message= f"Item not Found, Exception = {e}" )

    def delete( self, item_id ):
        try:
            op = items.pop( item_id )
            return op, 202
        except KeyError as e:
            abort( 404, message= f"Item not Found having item_id = { item_id }" )

    @blp.arguments( ItemUpdateSchema )
    def put( self, put_item_data, item_id ):

        items[ item_id ]["item_name"] = put_item_data["item_name"]
        items[ item_id ]["item_price"] = put_item_data["item_price"]

        if("store_id" in put_item_data):
            items[ item_id ]["store_id"] = put_item_data["store_id"]
            
        return items[ item_id ], 202
    
@blp.route('/addItem')
class AddItem(MethodView):
    @blp.arguments( ItemSchema )
    # def post(self):
    def post(self, item_data):
        
        for each_item in items.values():
            if( ( each_item["store_id"] == item_data["store_id"] )
            and ( each_item["item_name"] == item_data["item_name"] ) ):
                abort( 404, message= f"Duplicate Item present in store_id : { item_data['store_id'] }" )
        
        item_id = uuid.uuid4().hex
        item_data["item_id"] = item_id

        items[item_id] = item_data
        
        return item_data, 201

@blp.route("/items")
class Items( MethodView ):
    def get( self ):
        return items, 200