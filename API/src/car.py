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
        return {self.make: {self.model: self.car_class}}


#
#
# manufacturer_dict = {}
#     for row in list_of_rows:
#         car_object = Car.car_from_string(row)
#         car_data = {car_object.model: car_object.car_class}
#
#         try:
#             manufacturer_dict[car_object.make].append(car_data)
#         except KeyError:
#             manufacturer_dict[car_object.make] = []
#             manufacturer_dict[car_object.make].append(car_data)
#     return manufacturer_dict
