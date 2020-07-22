from tika import parser

from API.src.car import Car

file_loaction = '/Users/jacob.scheuer/Development/python/AutoXCalc/API/data/carClasses.pdf'
current_year = ' 2020'
disclaimer_length = 4
two_word_names = ["Alfa Romeo", "Aston Martin", "General Motors", "Tesla Motors"]


def parse_pdf_rows_into_list_of_strings(file_path):
    raw = parser.from_file(file_path)
    data = raw['content']
    rows_from_pdf = data.split('\n')
    non_blank_rows = [row for row in rows_from_pdf if row != '']
    rows_with_no_headers = [non_blank_row for non_blank_row in non_blank_rows if not current_year in non_blank_row]
    rows_with_no_footers = [no_header_row for no_header_row in rows_with_no_headers if not "Page" in no_header_row]
    clean_data = rows_with_no_footers[:-4]
    list_of_rows = [change_two_word_manufacturers_to_single_string(data_row) for data_row in clean_data]
    return list_of_rows


def change_two_word_manufacturers_to_single_string(data_row):
    for manufacturer in two_word_names:
        data_row = data_row.replace(manufacturer, manufacturer.replace(" ", "_"))
    return data_row


def change_list_of_strings_to_manufacturer_dict(list_of_rows):
    manufacturer_dict = {}
    for row in list_of_rows:
        car_object = Car.car_from_string(row)
        car_data = {car_object.model: car_object.car_class}

        try:
            manufacturer_dict[car_object.make].append(car_data)
        except KeyError:
            manufacturer_dict[car_object.make] = []
            manufacturer_dict[car_object.make].append(car_data)
    return manufacturer_dict
