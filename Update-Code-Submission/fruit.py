from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.main import create_app, db
from app.main.controller.order_controller import api
import unittest
import os

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.register_blueprint(api)
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
