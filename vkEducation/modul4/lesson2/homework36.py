from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(
    values_list_1: List[int], values_list_2: List[int]
) -> List[Tuple[int, int]]:
    result = []
    for val1, val2 in zip_longest(values_list_1, values_list_2, fillvalue=1):
        result.append((val1, val2))
    return result


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
