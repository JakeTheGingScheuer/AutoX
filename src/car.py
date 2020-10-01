class Car:
    def __init__(self, make="", model="", car_class=""):
        self.make = make
        self.model = model
        self.car_class = car_class

    def __eq__(self, other):
        return self.make == other.make and self.model == other.model and self.car_class == other.car_class

    @staticmethod
    def car_from_string(string_of_car):
        car = Car()
        split_row = string_of_car.split(' ', 1)
        car.make = split_row[0]
        car_data = split_row[1]

        try:
            model_and_class = car_data[:-10].rsplit(' ', 1)
            car.model = model_and_class[0]
            car.car_class = str(model_and_class[1] + " Street")

        except IndexError:
            car.model = "Not Listed"
            car.car_class = "H Street"

        if "ineligible" in car_data:
            car.car_class = "ineligible"

        return car

    def to_mongo(self):
        return {"make": self.make,
                "model": self.model,
                "car_class": self.car_class}

    @staticmethod
    def from_mongo(document):
        car = Car()
        car.make = document["make"]
        car.model = document["model"]
        car.car_class = document["car_class"]
        return car
