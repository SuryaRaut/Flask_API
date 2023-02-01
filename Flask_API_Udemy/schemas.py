# The marshmallow1 library is used to define data fields, and then to pass 
# incoming data through the validator. We can also go the other way round, and give it a Python 
# object which marshmallow then turns into a dictionary.

from marshmallow import Schema, fields

# Writing the ItemSchema marshmallow
class ItemSchema(Schema):
    # Paramter names should be same as what we pass in postman for adding item.

    id = fields.Str(dump_only=True)             # item_id, dump_only=True means that this field won't be used or expected
    item_name = fields.Str(required=True)       # item_name, required=True menas if the fields are not present, an error will be raised.
    item_price = fields.Float(required=True)    # item_price
    store_id = fields.Str(required=True)        # store_id linked with Item

# marshmallow will also check the data type with fields.Float and fields.Int

# When we want to update an Item, we have different requirements than when we want to create an item.
# The main difference is that the incoming data to our API when we update an item is different than 
# when we create one. Fields are optional, such that not all item fields should be required. Also, 
# you may not want to allow certain fields at all.

class ItemUpdateSchema(Schema):
    # Paramter names should be same as what you pass in postman for adding item.

    item_name = fields.Str()
    item_price = fields.Float()
    store_id = fields.Str()

    # This schema will only be used for incoming data, and we will never receive an id
    # We don't want clients to be able to change the store_id of an item. 
    # If we want to allow this, we can add the store_id field here

class StoreSchema(Schema):
    store_id = fields.Str(dump_only=True)
    store_name = fields.Str(required=True)
    store_type = fields.Str(required=True)
    

class StoreUpdateSchema(Schema):
    store_id = fields.Str(dump_only=True)
    store_name = fields.Str(required=True)
