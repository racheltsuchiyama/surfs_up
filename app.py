from flask import Flask

# Define flask app
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

