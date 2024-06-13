def filter_by_state(unfiltered_state_input: list) -> str:
    dictionary_1 = []
    dictionary_2 = []
    for item in unfiltered_state_input:
        for key, value in item.items():
            if value == "EXECUTED":
                dictionary_1.append(item)
            elif value == "CANCELED":
                dictionary_2.append(item)
    return f"{dictionary_1}\n{dictionary_2}"


def sort_by_date(unsorted_date_input: list[dict[str]]) -> list[dict[str]]:
    sorted_data = sorted(unsorted_date_input, key=lambda x: x["date"], reverse=True)
    return sorted_data
