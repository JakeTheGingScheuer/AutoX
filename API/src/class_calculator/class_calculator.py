import json

BACKUP_DATA_LOCATION = '/Users/jacob.scheuer/Development/python/AutoXCalc/API/src/cars.json'

class ClassCalculator:
    def __init__(self, data_location):
        self.data_location = data_location
        with open(self.data_location) as file:
          self.data = json.load(file)
        self.manufactuers = self.data["manufactuers"]

    def get_manufacturers(self):
        return self.manufactuers

    def add_manufacturer(self, name_of_manufactuer):
        self.manufactuers.append(name_of_manufactuer)

    def remove_manufacturer(self, name_of_manufactuer):
        self.manufactuers.remove(name_of_manufactuer)

    def save_changes(self):
        with open(self.data_location, 'w') as file:
            self.data = {"manufactuers" : self.manufactuers}
            changes = json.dumps(self.data)
            file.write(changes)

    def restore_data(self):
        with open(BACKUP_DATA_LOCATION) as file:
            self.data = json.load(file)
        self.manufactuers = self.data["manufactuers"]
        self.save_changes()
