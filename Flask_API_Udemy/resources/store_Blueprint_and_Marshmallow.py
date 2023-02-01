import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db_V1 import stores
from schemas import StoreSchema, StoreUpdateSchema

blp = Blueprint( 'stores', __name__, description="Opeations on stores" )
# The Blueprint arguments are the same as the Flask Blueprint1, with an added optional description keyword argument:
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

    @blp.arguments( StoreUpdateSchema )
    def put( self, put_store_data, store_id ):
    # def put( self, store_id ):
        # put_store_data = request.get_json()

        if( not stores.get( store_id ) ):
            abort( 404, message= f"Item not Found having store_id = { store_id }" )
        
        """
        if( "store_name" not in put_store_data ):
            abort( 404, message= f"API does not have required parameters" )
        """

        stores[ store_id ]["store_name"] = put_store_data["store_name"]

        return stores[ store_id ], 202
    
@blp.route('/addStore')
class AddStore(MethodView):
    
    @blp.arguments( StoreSchema )
    def post(self, store_data): # We need to keep Marshmallow argument at the 2nd place just after self.
                                # as we are implementing Marshmallow technique. So Marshmallow will give the data to argument
                                # in order to validate data using blp.arguments( StoreSchema ) decorator and then, allows
                                # Python to proceed further if everything looks good.
        
        # store_data = request.get_json() # As we are getting item_data details. So, request.get_json() is not required
        
        """
        if( ("store_name" not in store_data) and ("store_type" not in store_data) ):
            abort( 404, message= f"API does not have required parameters" )
        """

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

"""
@blp.route("/duplicateStore")
class DuplicateStore:
    def get(self):
        unique_stores = []
        duplicate_store = {}

        for each_store in stores.values():
            current_store_data = [ each_store["store_name"], each_store["store_type"] ]

            if( current_store_data not in unique_stores):
                unique_stores.append( current_store_data )
            else:
                print( f'Before, each_store["store_id"] = { each_store["store_id"] } and duplicate_store = { duplicate_store }\n\n' )
                
                if( each_store["store_name"] not in duplicate_store ):
                    duplicate_store[ each_store["store_name"] ] = [ 
                            { "store_type" : each_store["store_type"] 
                            ,"count" : 2 }
                            ]

                else:
                    type_not_present = True
                    for i in duplicate_store[ each_store["store_name"] ]:
                        print( i )
                        if( i["store_type"] == each_store["store_type"] ):
                            i["count"] += 1
                            type_not_present = False

                    if( type_not_present ):
                        duplicate_store[ each_store["store_name"] ].append( 
                            { "store_type" : each_store["store_type"] 
                            ,"count" : 2 } 
                            )

                print( f'After, each_store["store_id"] = { each_store["store_id"] } and duplicate_store = { duplicate_store }\n\n' )

        return duplicate_store, 200
"""