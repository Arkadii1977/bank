from widget import card_number_input
from widget import account_input
from widget import card_type
from widget import get_data
from widget import user_date_input


def get_mask_card_number(card_number: str) -> str:
    """функция возвращает маску карты"""
    masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked_card_number


def get_mask_account(mask_account: str) -> str:
    """функция возвращает маску счета"""
    masked_account = "**" + mask_account[16:]
    return masked_account


"""Проверяем что у нас на входе: номер карты или номер счета и выводим в зашифрованном виде """
if card_type != "Счет":
    print(card_type, get_mask_card_number(card_number_input))
elif card_type == "Счет":
    print(card_type, get_mask_account(account_input))
"""Выводим дату"""
print(get_data(user_date_input))
