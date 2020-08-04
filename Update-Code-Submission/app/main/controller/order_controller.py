from flask import Flask, request, jsonify, make_response, abort
from app.main import db
from app.main.model.order import Order
from flask import Blueprint

api = Blueprint('api', __name__, template_folder='templates')

# Endpoint to place new order
@api.route("/order", methods=['POST'])
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
@api.route("/report", methods=['GET'])
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

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def formatNumber(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num
        