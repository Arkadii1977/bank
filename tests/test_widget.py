import pytest

from src.widget import get_data, mask_account_card


def test_get_data(date):
    assert get_data("2018-07-11T02:26:18.671407") == date


@pytest.mark.parametrize("value, expected", [
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589")
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected
