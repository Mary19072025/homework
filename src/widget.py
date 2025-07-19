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


def get_data(data:str)->str:
  data_1 = data[:10]
  data_2 = data_1.split('-')
  return f"{data_2[2]}.{data_2[1]}.{data_2[0]}"


data = str('20251707')
print(get_data(data))
