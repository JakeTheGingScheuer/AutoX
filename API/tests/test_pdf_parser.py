from API.src.pdf_parse import *


def test_change_two_word_manufacturers_to_single_string():
    test_row = "Alfa Romeo 164 1991-93 non-S H Street HS"
    expected = "Alfa_Romeo 164 1991-93 non-S H Street HS"

    actual = change_two_word_manufacturers_to_single_string(test_row)
    assert actual == expected


def test_parse_pdf_rows_into_list_of_strings():
    file_loaction = '/Users/jacob.scheuer/Development/python/AutoXCalc/API/data/carClasses.pdf'
    actual = extract_pdf_rows_into_list_of_strings(file_loaction)[0]
    expected = "Acura CL H Street HS"
    assert actual == expected


def test_change_list_of_strings_to_manufacturer_dict():
    file_location = '/Users/jacob.scheuer/Development/python/AutoXCalc/API/data/carClasses.pdf'
    list_of_rows = extract_pdf_rows_into_list_of_strings(file_location)
    man_dict = change_list_of_strings_to_list_of_cars(list_of_rows)
    actual = man_dict["Acura"]
    expected = [{'CL': 'H Street'},
                {'ILX': 'H Street'},
                {'Integra 1986-2001 excluding Type R': 'H Street'},
                {'Integra Type R': 'D Street'},
                {'Legend': 'H Street'},
                {'NSX 2017-20': 'Super Street'},
                {'NSX non-Zarnardi Edition': 'B Street'},
                {'NSX Alex Zanardi Signature Edition': 'A Street'},
                {'RLX': 'G Street'},
                {'RSX + Type S': 'H Street'},
                {'TL': 'H Street'},
                {'TLX': 'G Street'},
                {'TSX': 'H Street'},
                {'Vigor': 'H Street'}]
    assert actual == expected


def test_print_out_data():
    file_location = '/Users/jacob.scheuer/Development/python/AutoXCalc/API/data/carClasses.pdf'
    list_of_rows = extract_pdf_rows_into_list_of_strings(file_location)
    man_dict = change_list_of_strings_to_list_of_cars(list_of_rows)
    for i in man_dict.keys():
        print(i)
        for x in man_dict[i]:
            print(f"-----------{x}")
    assert 1 == 1
