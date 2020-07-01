#!flask/bin/python
import os
from flask import Flask
from src.class_calculator.class_calculator import ClassCalculator

DATA_LOCATION = os.getcwd()+'/data/cars.json'

calculator = ClassCalculator(DATA_LOCATION)
app = Flask(__name__)

@app.route('/')
def index():
    return 'React App coming soon', 200

@app.route('/api/data')
def get_car_data():
    return calculator.data, 200

@app.route('/api/data', methods=['POST'])
def add_car_data():
    data = request.get_data
    calculator.add_data(data)
    return 'Need Some Validation Here', 200
