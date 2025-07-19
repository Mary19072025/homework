def get_mask_card_number(card_number: str) -> str:
    """ Функция маскировки номера карты"""
    masked_number = (f"{card_number[:4]} "
                     f"{card_number[4:6]}** **** "
                     f"{card_number[-4:]}")
    return masked_number

card_number =str(2200456978964585)
print(get_mask_card_number(card_number))


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета"""
    masked_account = f"**{account_number[-4:]}"
    return masked_account


account_number = str(9875968965896321)
print(get_mask_account(account_number))
