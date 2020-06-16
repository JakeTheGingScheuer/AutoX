import json


class ClassCalculator:
    def __init__(self, data_location):
        with open(data_location) as file:
          self.data = json.load(file)
        self.manufactuers = self.data["manufactuers"]

    def get_manufacturers(self):
        return self.manufactuers

    def add_manufacturer(self, name_of_manufactuer):
        self.manufactuers.append(name_of_manufactuer)
