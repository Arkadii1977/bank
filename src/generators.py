def filter_by_currency(money_move, currency):
    """Функция принимает список словарей и возвращает по очереди операции, в которых указана заданная валюта"""
    for action in money_move:
        if action.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield action


def transaction_descriptions(money_move):
    """Функция принимает список словарей и возвращает описание каждой операции по очереди"""
    for action in money_move:
        yield action['description']


def card_number_generator(start, stop):
    """Функция генерирует номера карт в заданном диапазоне"""
    for num in range(start, stop+1):
        card_num = '{:016d}'.format(num)
        formatted_card_num = ' '.join([card_num[i:i+4] for i in range(0, len(card_num), 4)])
        yield formatted_card_num
