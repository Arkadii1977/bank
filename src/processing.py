def filter_by_state(unfiltered_state_input, state="EXECUTED"):
    """Функция фильтрует список словарей по значению ключа state и возвращает новый список"""
    dictionary = []
    for item in unfiltered_state_input:
        for key, value in item.items():
            if value == state:
                dictionary.append(item)
    return dictionary


def sort_by_date(unsorted_date_input: list) -> list:
    """Функция филтрует список транзакций по датам и возвращает их же в отсортированном виде"""
    sorted_data = sorted(unsorted_date_input, key=lambda x: x["date"], reverse=True)
    return sorted_data


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "CANCELED"))
