string = input().lower()

string = string.replace(" ", "")

unique_chairs = sorted(set(string))

result = " ".join(unique_chairs)

print(result)
