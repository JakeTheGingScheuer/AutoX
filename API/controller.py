#!flask/bin/python
from flask import Flask
import class_calculator.class_calculator as class_calculator

app = Flask(__name__)

@app.route('/')
def index():
    return class_calculator.get_manufacturers()
