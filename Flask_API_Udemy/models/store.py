from db import db

# Every model inherits from db.Model. That way when we tell SQLAlchemy about them (in Configure Flask-SQLAlchemy))
class StoreModel( db.Model ):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)            
    name = db.Column(db.String(80), unique=False, nullable=False)
    type = db.Column(db.String(80), unique=False, nullable=False)
