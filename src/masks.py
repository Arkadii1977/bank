'''
def get_mask_card_number(card_number: str) -> str:
    """функция возвращает маску карты"""
    masked_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked_card_number


def get_mask_account(mask_account: str) -> str:
    """функция возвращает маску счета"""
    masked_account = "**" + mask_account[16:]
    return masked_account


"""Вводим данные карты и аккаунта"""
card_number_input: str = input()
account_input: str = input()

print(get_mask_card_number(card_number_input))
print(get_mask_account(account_input))
'''
