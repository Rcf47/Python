def cache_deco(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@cache_deco
def solution(func_map, func_filter, data):
    for i, item in enumerate(data):
        if func_filter(item):
            if i % 2 == 1:
                yield func_map(item)


# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)


def calc():
    count = 0

    @cache_deco
    def calc_(x):
        nonlocal count
        count += 1
        print("Call:", count)
        return x

    return calc_


for i in solution(calc(), lambda x: x % 2 == 1, (1, 1, 2, 2, 2, 3, 1, 2, 3, 1)):
    print(i)


# def calc():
#     count = 0
#
#     def calc_(x):
#         nonlocal count
#         count += 1
#         print("Call:", count)
#         return x
#
#     return calc_
#
#
# for i in solution(calc(), lambda x: x % 2 == 1, (1, 1, 2, 2, 2, 3, 1, 2, 3, 1)):
#     print(i)
