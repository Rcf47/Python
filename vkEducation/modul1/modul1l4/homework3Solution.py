left_boundary = int(input())
right_boundary = int(input())

numbers = []
while True:
    number_input = input()
    if number_input == "":
        break
    number = int(number_input)
    numbers.append(number)

all_in_range = all(left_boundary <= number <= right_boundary for number in numbers)

if all_in_range:
    print(True)
else:
    print(False)
