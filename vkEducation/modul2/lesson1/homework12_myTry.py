def calc(string):
    nums = list(map(int, string.split()))
    average = sum(nums) / len(nums)
    return average


while True:
    string = input()
    if string == "":
        break
    print(calc(string))
