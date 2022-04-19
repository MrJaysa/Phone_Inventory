from flask_sqlalchemy         import SQLAlchemy
from datetime                 import datetime, timedelta, date
from time                     import time
from secrets                  import token_hex
from shortuuid                import ShortUUID

db = SQLAlchemy()

class Store(db.Model):
    __name__            = 'store'

    id               	= db.Column(db.Integer,     primary_key=True)
    item_name           = db.Column(db.Text,        nullable=True)
    price               = db.Column(db.Float,       default=0.0)
    public_key     	    = db.Column(db.Text,        nullable=True, default=lambda:ShortUUID().random(4) + str(time()).replace('.', '') + token_hex(3))
    created_on          = db.Column(db.DateTime,    default=datetime.utcnow)

    def create(self, item, price):
        self.item_name = item
        self.price     = price
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
