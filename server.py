#!flask/bin/python
import os
from flask import Flask, jsonify
from flask_cors import CORS
from src.api import Api

api = Api()

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/street_class/')
def get_street_class_data():
    cars = api.get_car_data()
    return jsonify(cars), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)
