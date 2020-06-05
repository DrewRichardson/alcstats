from flask import Flask           # import flask
from models import Schema
app = Flask(__name__)             # create an app instance

if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)                     # run the flask app