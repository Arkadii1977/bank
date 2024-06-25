import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize("value_first, value_second, expected", [
        (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003'])])
def test_card_number_generator(value_first, value_second, expected):
        ls = []
        for card_number in card_number_generator(1, 3):
                ls.append(card_number)
        assert ls == expected
