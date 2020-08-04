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
    Open the following Url or other appropriate url in your local machine after building app 
    http://localhost:5000/
    Using following api to place an order
    http://localhost:5000/order (POST)
    with json sample 
    {
        "date": 3,
        "fruits": {
        "orange": 10,
        "apple": 3,
        "coconut": 10
        }
    }
    Use this following api to get report
    http://localhost:5000/report?from={a}&to={b} (GET) where a and b are integer

### Docker ###
    Run following commands to create docker image
    > docker image build -t fruit-store-application .
    > docker run -p 5001:5000 -d fruit-store-application
    Check docker container
    > docker container ls
    > open docker desktop (Windows 10) and view url to test or open docker log to view url: 
    > docker container ls
    > docker container logs [container id]