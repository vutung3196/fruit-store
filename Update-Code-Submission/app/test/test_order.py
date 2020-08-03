from app.main import db
from fruit import app
from app.main.model.order import Order
from app.test.base import BaseTestCase
from app.main.controller.order_controller import place_order, get_report
import json
import unittest

class TestOrderController(BaseTestCase):
    def test_report_order(self):
        order = Order(
            fruitName='apple',
            quantity=10,
            date=1
        )
        order_second = Order(
            fruitName='apple',
            quantity=20,
            date=2
        )
        result = {
            "apple": 30, 
        }
        db.session.add(order)
        db.session.add(order_second)
        db.session.commit()
        response = self.client.get('/report?from=1&to=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(result), len(response.json['data']))
        assert result ==  response.json['data']

    def test_place_order(self):
        fruits = {
            "apple": 30, 
            "orange": 10
        }
        result = {
            "apple": 30, 
            "orange": 10
        }

        response = self.client.post('/order', data=json.dumps(dict(date = 1, fruits = fruits)), 
        headers={'Content-Type': 'application/json'})
        resultResponse = self.client.get('/report?from=1&to=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'place order successfully')
        self.assertEqual(len(result), len(resultResponse.json['data']))
        assert result ==  resultResponse.json['data']

if __name__ == '__main__':
    unittest.main()

