start, end, step = map(int, input().split())

result = list(map(lambda x: x**2 if x % 2 != 0 else -x, range(start, end, step)))
for num in result:
    print(num)
