string = input()
average_length = round(
    sum(len(word) for word in string.split()) / len(string.split()), 2
)
print(average_length)
