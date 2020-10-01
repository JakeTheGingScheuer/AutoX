from src.mongo_controller import MongoController


class Api:
    def __init__(self, mongo=None):
        self.mongo = mongo or MongoController()
        self.mongo.populate_mongo()

    def get_car_data(self):
        json_response = {"manufacturers": []}
        manufacturer2model2class = self.mongo.get_manufacturer_dict()

        for manufacturer in manufacturer2model2class:
            car_models = []
            models2classes = manufacturer2model2class[manufacturer]

            for carModel in models2classes:
                car_models.append({"name": carModel, "carClass": models2classes[carModel]})
            json_response["manufacturers"].append({"name": manufacturer, "carModels": car_models})

        return json_response
