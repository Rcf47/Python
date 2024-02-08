from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    queue = deque(nums)
    queue.rotate(n)
    return list(queue)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
