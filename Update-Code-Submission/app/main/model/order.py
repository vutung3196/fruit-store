from .. import db
from sqlalchemy.orm import validates

class Order(db.Model):
    __tablename__ = 'order'
    orderId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fruitName = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    date = db.Column(db.Integer, nullable=False)

    @validates('quantity')
    def validate_quantity(self, key, quantity):
        if quantity <= 0:
            raise ValueError('Quantity must be greater than 0')
        return quantity

    def __init__(self, fruitName, quantity, date):
        self.fruitName = fruitName
        self.quantity = quantity
        self.date = date