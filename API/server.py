#!flask/bin/python
import os
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from API.src.mongo_controller import MongoController

mongo_controller = MongoController()
app = Flask(__name__)
mongo_controller.populate_mongo()

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/street_class/')
def get_street_class_data():
    cars = mongo_controller.get_manufacturer_dict()
    return jsonify(cars), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)
