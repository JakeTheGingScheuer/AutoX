from src.car import Car
from src.mongo_wrapper import MongoWrapper
from src.pdf_parse import parse_pdf_to_car_list


class MongoController:
    def __init__(self):
        self.mongo = MongoWrapper("AutoX")

    def populate_mongo(self):
        self.mongo.use_database("AutoX")
        self.mongo.drop_collection("StreetClass")
        car_list = parse_pdf_to_car_list()
        self.mongo.use_collection("StreetClass")
        for car in car_list:
            self.mongo.insert_one(car.to_mongo())

    def get_manufacturer_dict(self):
        self.mongo.use_database("AutoX")
        self.mongo.use_collection("StreetClass")
        query_result = self.mongo.find({})

        car_list = []
        for document in query_result:
            car_list.append(Car.from_mongo(document))
        manufacturer_dict = {}

        for car in car_list:
            try:
                manufacturer_dict[car.make][car.model] = car.car_class
            except KeyError:
                manufacturer_dict[car.make] = {}
                manufacturer_dict[car.make][car.model] = car.car_class

        return manufacturer_dict
