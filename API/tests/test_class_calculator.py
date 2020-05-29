import pytest
import class_calculator.class_calculator as class_calculator

def test_get_manufacturers_responds_with_200_OK():
    assert ({
        "manufacturers" : [
            "Honda",
            "Subaru",
            "Toyota"
        ]
    }, 200) == class_calculator.get_manufacturers()
