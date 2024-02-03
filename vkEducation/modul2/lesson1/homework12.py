def calc(string):
    nums = list(map(int, string.split()))
    summ = sum(nums)
    return summ / len(nums)


while string := input():
    print(calc(string))
