string = input()

has_a_or_o = False
has_e_or_i = False

for char in string:
    if char == "a" or char == "o":
        has_a_or_o = True
    if char == "e" or char == "i":
        has_e_or_i = True

if has_a_or_o and not has_e_or_i:
    print(True)
else:
    print(False)
