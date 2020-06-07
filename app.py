from flask import Flask, request, jsonify, render_template        # import flask
from models import Schema
from service import AlcStatsService

app = Flask(__name__)             # create an app instance

@app.route("/")
def hello():
    return "Hey!"

@app.route("/alcstats", methods=["GET"])
def list_todo():
    return render_template("stats.html")

@app.route("/alcstats", methods=["POST"])
def create_todo():
    print("request is " + request.get_json())
    return jsonify(AlcStatsService().create(request.get_json()))

if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)                     # run the flask app