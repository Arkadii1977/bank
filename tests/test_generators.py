import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }])


@pytest.mark.parametrize("value_first, value_second, expected", [
        (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003'])])
def test_card_number_generator(value_first, value_second, expected):
    ls = []
    for card_number in card_number_generator(1, 3):
        ls.append(card_number)
    assert ls == expected


@pytest.mark.parametrize("value, expected", [(transactions, ["Перевод организации", "Перевод со счета на счет"])])
def test_transaction_descriptions(value, expected):
    ls = []
    descriptions = transaction_descriptions(transactions)
    for transaction in descriptions:
        ls.append(transaction)
    assert ls == expected


@pytest.mark.parametrize("value_first, value_second, expected", [(transactions, "USD", [939719570, 142264268])])
def test_filter_by_currency(value_first, value_second, expected):
    ls = []
    usd_transactions = filter_by_currency(transactions, "USD")
    for transaction in usd_transactions:
        ls.append(transaction["id"])
    assert ls == expected
