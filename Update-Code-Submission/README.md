### Terminal commands ###
Note: make sure you have `pip` installed.

    > Initial installation: pip install -r requirements.txt;

    > To run test: python fruit.py test

    > To run application: python fruit.py run

Make sure you run the initial migration commands to update the database when model changes.
    
    > python fruit.py db init

    > python fruit.py db migrate --message 'initial database migration'

    > python fruit.py db upgrade

### View the app ###
    Open the following Url
    http://localhost:5000/
    Using following api to place an order and get report
    http://localhost:5000/order (POST)
    http://localhost:5000/report?from=1&to=10 (GET)

### Docker ###
    Run following commands to create docker image
    > docker image build -t fruit-store-application .
    > docker run -p 5001:5000 -d fruit-store-application
    Check docker container
    > docker container ls
    > open docker desktop and view url to test