import pytest
import os

from class_calculator import ClassCalculator


class TestClassCalculator(object):

    data_location = os.getcwd()+'/data/test_data.json'
    uut = ClassCalculator(data_location)

    def teardown_method(self):
        self.uut.restore_data()

    def test_get_manufacturers_returns_list_of_manufacturers_from_json(self):
        list_of_manufacturers = self.uut.get_manufacturers()
        assert type(list_of_manufacturers) is list

    def test_add_manufacturer_adds_manufacturer_to_list(self):
        self.uut.add_manufacturer("Bugatti")
        list_of_manufacturers = self.uut.get_manufacturers()
        assert "Bugatti" in list_of_manufacturers

    def test_remove_manucaturer_removes_manufacturer_to_list(self):
        self.uut.add_manufacturer("Bugatti")
        self.uut.remove_manufacturer("Bugatti")
        list_of_manufacturers = self.uut.get_manufacturers()
        assert "Bugatti" not in list_of_manufacturers

    def test_save_changes_updates_storage(self):
        self.uut.add_manufacturer("Bugatti")
        self.uut.save_changes()

        self.uut = ClassCalculator(self.data_location)
        list_of_manufacturers = self.uut.get_manufacturers()
        assert "Bugatti" in list_of_manufacturers

    def test_restore_data_rolls_back_data(self):
        self.uut.remove_manufacturer("Acura")
        self.uut.restore_data()
        list_of_manufacturers = self.uut.get_manufacturers()
        assert "Acura" in list_of_manufacturers

    def test_add_data_calls_add_manufacturer(self):
        fake_json = {"manufactuers":"Mosler"}
        self.uut.add_data(fake_json)
        list_of_manufacturers = self.uut.get_manufacturers()
        assert "Mosler" in list_of_manufacturers
