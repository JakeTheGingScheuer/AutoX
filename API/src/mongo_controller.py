from API.src.car import Car
from API.src.mongo_wrapper import MongoWrapper
from API.src.pdf_parse import parse_pdf_to_car_list


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
                manufacturer_dict[car.make].append(car.car_data())
            except KeyError:
                manufacturer_dict[car.make] = [car.car_data()]

        return manufacturer_dict
