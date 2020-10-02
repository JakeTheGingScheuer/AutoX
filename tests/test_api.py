from src.api import Api
from src.car import Car

fake_car_list = [
    Car(make="Honda", model="Civic", car_class="HS"),
    Car(make="Honda", model="Accord", car_class="GS"),
    Car(make="Subaru", model="BRZ", car_class="DS"),
    Car(make="Subaru", model="WRX", car_class="DS")
]


def test__get_car_data__returns_formatted_json():
    subject = Api(fake_car_list)

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
