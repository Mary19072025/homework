def filter_by_state(list_of_dict: list, state='EXECUTED') -> list:
    filtered_list = []

    for dict_item in list_of_dict:

        if dict_item.get('state') == state:
            filtered_list.append(dict_item)

    return filtered_list

list_of_dict =[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
print(filter_by_state(list_of_dict))


from datetime import datetime


def sort_by_date(data_list: list, data_key='date', descending=True) -> list:

    ''' Функция, которая принимает список словарей и необязательный параметр,

    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать

     новый список, отсортированный по дате (date).'''

    return sorted(data_list, key=lambda x: datetime.fromisoformat(x[data_key]), reverse=descending)

data_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
print(sort_by_date(data_list))


