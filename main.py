#!flask/bin/python
from flask import Flask, jsonify
from flask_cors import CORS
from src.api import Api

api = Api()

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return 'server is up'


@app.route('/street_class')
def get_street_class_data():
    cars = api.get_car_data()
    return jsonify(cars), 200


if __name__ == "__main__":
    app.run(debug=True)
