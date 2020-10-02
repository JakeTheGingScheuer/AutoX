from data.extracted_data import cars
from src.car import Car

extracted_data = cars


class Api:

    def __init__(self, cars_from_pdf=None):
        self.car_list = cars_from_pdf or self.change_list_of_strings_to_list_of_cars()

    def get_car_data(self):
        manufacturer2model2class = self.group_cars_by_make()
        json_response = self.convert_car_dict_to_json(manufacturer2model2class)
        return json_response

    def group_cars_by_make(self):

        manufacturer2model2class = {}
        for car in self.car_list:
            try:
                manufacturer2model2class[car.make][car.model] = car.car_class
            except KeyError:
                manufacturer2model2class[car.make] = {}
                manufacturer2model2class[car.make][car.model] = car.car_class

        return manufacturer2model2class

    def convert_car_dict_to_json(self, car_dict):
        json_response = {"manufacturers": []}

        for manufacturer in car_dict:
            car_models = []
            models2classes = car_dict[manufacturer]

            for carModel in models2classes:
                car_models.append({"name": carModel, "carClass": models2classes[carModel]})
            json_response["manufacturers"].append({"name": manufacturer, "carModels": car_models})

        return json_response

    def change_list_of_strings_to_list_of_cars(self):
        car_list = []
        for row in cars:
            car_object = Car.car_from_string(row)
            car_list.append(car_object)
        return car_list
