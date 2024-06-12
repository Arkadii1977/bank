from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(card_input: str) -> str:
    """Функция возвращает номер карты или номер счета"""
    card_information = card_input.split()
    if len(card_information) == 3:
        card_number = card_information[2]
        result = card_information[0] + " " + card_information[1] + " " + get_mask_card_number(card_number)
        return result
    elif "Счет" in card_information:
        bill_number = card_information[1]
        result = card_information[0] + " " + get_mask_account(bill_number)
        return result
    else:
        card_number = card_information[1]
        result = card_information[0] + " " + get_mask_card_number(card_number)
        return result


def get_data(date_input: str) -> str:
    """Функция возвращает преобразованную дату и время"""
    year = date_input[:4]
    month = date_input[5:7]
    day = date_input[8:10]
    result = day + "." + month + "." + year
    return result


card_or_bill_input: str = input()
date_user_input: str = input()
print(mask_account_card(card_or_bill_input))
print(get_data(date_user_input))
