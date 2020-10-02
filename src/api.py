from src.pdf_parse import parse_pdf_to_car_list


class Api:

    def __init__(self, cars_from_pdf=None):
        self.car_list = cars_from_pdf or parse_pdf_to_car_list()

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
