def filter_by_state(unfiltered_state_input, state: list) -> list:
    """Функция фильтрует список словарей по значению ключа state и возвращает новый список"""
    dictionary = []
    for item in unfiltered_state_input:
        for key, value in item.items():
            if value == state:
                dictionary.append(item)
    return dictionary


def sort_by_date(unsorted_date_input: list[dict[str]]) -> list[dict[str]]:
    """Функция филтрует список транзакций по датам и возвращает их же в отсортированном виде"""
    sorted_data = sorted(unsorted_date_input, key=lambda x: x["date"], reverse=True)
    return sorted_data
