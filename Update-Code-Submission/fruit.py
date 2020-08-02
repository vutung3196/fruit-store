from flask import Flask, request, jsonify, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from util import isInt, formatNumber
import datetime
import os

# Create an instance of web application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(basedir, 'fruit.sqlite')

# Initialize database
db = SQLAlchemy(app)

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

# Endpoint to create new fruit
@app.route("/order", methods=['POST'])
def place_order():
    if not request.json or not 'fruits' in request.json or not 'date' in request.json:
        abort(400)
    data = request.json
    fruits = data['fruits']
    for fruit in fruits:
        new_order = Order(
            date = data['date'], 
            fruitName = fruit.lower(),
            quantity = fruits[fruit],
        )
        db.session.add(new_order)
    db.session.commit()
    return jsonify({'message':'place order successfully'})    

# Endpoint to get report of orders
@app.route("/report", methods=['GET'])
def get_report():
    start_date = request.args.get('from')
    end_date = request.args.get('to')
    if start_date is None or end_date is None:
        return make_response(jsonify({'error': 'Start date and end date are required'}), 404)
    if isInt(start_date) & isInt(end_date):
        start = int(start_date)
        end = int(end_date)
        if start > end:
            return make_response(jsonify({'error': 'Start date should be equal or greater than end date'}), 404)
        orders = Order.query.filter(Order.date.between(start_date, end_date))
        result = {}
        for order in orders:
            quantity = formatNumber(order.quantity)
            if order.fruitName in result:
                result[order.fruitName] += quantity
                continue
            result[order.fruitName] = quantity
        return jsonify({'data': result})
    return make_response(jsonify({'error': 'Start date and end date should be value of timestamp or integers'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
