# Import flask
from flask import Flask

# Create a new flask app instance
app = Flask(__name__)

# Create app route
@app.route('/')
def hello_world():
    return 'Hello world'
