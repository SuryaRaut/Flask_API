from db import db

# Every model inherits from db.Model. That way when we tell SQLAlchemy about them (in Configure Flask-SQLAlchemy))
# , it will know to look at them to create tables.
class ItemModel( db.Model ):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)            
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey( "stores.id" ) unique=False, nullable=False)
