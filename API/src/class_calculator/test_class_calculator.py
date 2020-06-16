import pytest
import os

from class_calculator import ClassCalculator


class TestClassCalculator(object):
    data_location = os.getcwd()+'/src/cars.json'
    uut = ClassCalculator(data_location)

    def test_get_manufacturers_returns_list_of_manufacturers_from_json(self):
        list_of_manufacturers = self.uut.get_manufacturers()
        assert type(actual) is list

    def test_add_manufacturer_adds_manufacturer_to_list(self):
        self.uut.add_manufacturer("Bugatti")
        list_of_manufacturers = self.uut.get_manufacturers()
        assert "Bugatti" in brands
