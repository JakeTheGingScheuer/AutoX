from mock import MagicMock

from src.api import Api

fake_car_data = {
    "Honda": {
        "Civic": "HS",
        "Accord": "GS"
    },
    "Subaru": {
        "BRZ": "DS",
        "WRX": "DS"
    }
}


def test__get_car_data__returns_formatted_json():
    fake_mongo = MagicMock()
    fake_mongo.get_manufacturer_dict = MagicMock(return_value=fake_car_data)
    subject = Api(fake_mongo)

    actual = subject.get_car_data()
    expected = {
              "manufacturers": [
                {
                  "name": "Honda",
                  "carModels": [
                    {
                      "name": "Civic",
                      "carClass": "HS"
                    },
                    {
                      "name": "Accord",
                      "carClass": "GS"
                    }
                  ]
                },
                {
                  "name": "Subaru",
                  "carModels": [
                    {
                      "name": "BRZ",
                      "carClass": "DS"
                    },
                    {
                      "name": "WRX",
                      "carClass": "DS"
                    }
                  ]
                }
              ]
            }

    assert actual == expected
