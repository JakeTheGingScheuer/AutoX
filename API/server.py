#!flask/bin/python
import os

from flask import Flask, render_template

from API.src.mongo_wrapper import MongoWrapper
from API.src.pdf_parse import parse_pdf_to_car_list

mongo = MongoWrapper("AutoX")
app = Flask(__name__)

car_list = parse_pdf_to_car_list()
mongo.use_database("AutoX")
mongo.use_collection("StreetClass")
for car in car_list:
    mongo_object = car.to_mongo()
    mongo.insert(mongo_object)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)
