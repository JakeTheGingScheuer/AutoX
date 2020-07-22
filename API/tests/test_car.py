from API.src.car import Car


def test_string_to_car():
    test_string = "Acura CL H Street HS"
    expected = Car("Acura", "CL", "H Street")

    actual = Car.car_from_string(test_string)
    assert actual == expected


def test_split_string_into_key_value_ineligible():
    test_string = "Acura CL ineligible"
    expected = Car("Acura", "CL", "ineligible")

    actual = Car.car_from_string(test_string)
    assert actual == expected
