from src.car import Car
from src.pdf_parse import *


def test_change_two_word_manufacturers_to_single_string():
    test_row = "Alfa Romeo 164 1991-93 non-S H Street HS"
    expected = "Alfa_Romeo 164 1991-93 non-S H Street HS"

    actual = change_two_word_manufacturers_to_single_string(test_row)
    assert actual == expected


def test_parse_pdf_rows_into_list_of_strings():
    file_loaction = '/Users/jacob.scheuer/Development/python/AutoXAPI/data/carClasses.pdf'
    actual = extract_pdf_rows_into_list_of_strings(file_loaction)[0]
    expected = "Acura CL H Street HS"
    assert actual == expected


def test_change_list_of_strings_to_list_of_cars():
    file_location = '/Users/jacob.scheuer/Development/python/AutoXAPI/data/carClasses.pdf'
    list_of_rows = extract_pdf_rows_into_list_of_strings(file_location)
    list_of_cars = change_list_of_strings_to_list_of_cars(list_of_rows)

    actual = list_of_cars[0]
    expected = Car(make="Acura", model="CL", car_class="H Street")

    assert actual == expected
    assert len(list_of_cars) == 901
