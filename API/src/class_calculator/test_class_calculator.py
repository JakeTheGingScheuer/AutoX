import pytest
import os

from class_calculator import ClassCalculator


class TestClassCalculator(object):
    data_location = os.getcwd()+'/src/cars.json'

    def test_get_manufacturers_returns_list_of_manufacturers_from_json(self):
        uut = ClassCalculator(self.data_location)
        list_of_manufacturers = uut.get_manufacturers()
        assert type(list_of_manufacturers) is list

    def test_add_manufacturer_adds_manufacturer_to_list(self):
        uut = ClassCalculator(self.data_location)
        uut.add_manufacturer("Bugatti")
        list_of_manufacturers = uut.get_manufacturers()
        assert "Bugatti" in list_of_manufacturers

    def test_remove_manucaturer_removes_manufacturer_to_list(self):
        uut = ClassCalculator(self.data_location)
        uut.add_manufacturer("Bugatti")
        uut.remove_manufacturer("Bugatti")
        list_of_manufacturers = uut.get_manufacturers()
        assert "Bugatti" not in list_of_manufacturers
