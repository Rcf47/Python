left = int(input())
right = int(input())

flag = True

while num := input():
    num = int(num)
    if left <= num < right:
        continue
    else:
        flag = False
        break


print(flag)
