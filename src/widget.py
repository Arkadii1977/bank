def mask_account_card(card_input: str) -> str:
    """Функция возвращает номер карты или номер счета"""
    card_information = card_input.split()
    if len(card_information) == 3:
        card_number = card_information[2]
        return card_number
    elif len(card_information) == 2:
        card_number = card_information[1]
        return card_number


def get_data(date: str) -> str:
    """функция возвращает дату"""
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    result = day + '.' + month + '.' + year
    return result


"""Вводим карту/счет"""
user_input: str = input()
"""Вводим дату"""
user_date_input: str = input()
"""Проверяем присутствует ли имя карты"""
card_info = user_input.split()
if len(card_info) == 3:
    name = card_info[:2]
    card_type = ' '.join(str(x) for x in name)
elif len(card_info) == 2:
    if "Счет" in card_info:
        card_type = "Счет"
    else:
        card_type = card_info[0]
card_number_input: str = mask_account_card(user_input)
account_input: str = mask_account_card(user_input)
