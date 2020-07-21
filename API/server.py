#!flask/bin/python
import os
from flask import Flask, render_template, request
from src.class_calculator.class_calculator import ClassCalculator

DATA_LOCATION = os.getcwd()+'/data/cars.json'

calculator = ClassCalculator(DATA_LOCATION)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/data')
def get_car_data():
    return calculator.data, 200


@app.route('/api/data', methods=['POST'])
def add_car_data():
    data = request.get_data()
    return data, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)
