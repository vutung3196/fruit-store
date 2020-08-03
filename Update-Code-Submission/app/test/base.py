from app.main import db
from fruit import app
from flask import Flask
from flask_testing import TestCase

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app
    
    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


