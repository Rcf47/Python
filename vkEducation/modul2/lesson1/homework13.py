def process_string(input_string):
    if input_string[0] == "!":
        processed_string = input_string[1:].upper()
    else:
        processed_string = input_string.lower()

    processed_string = (
        processed_string.replace("!", "")
        .replace("@", "")
        .replace("#", "")
        .replace("%", "")
    )

    return processed_string


while True:
    input_string = input()
    if input_string == "":
        break
    print(process_string(input_string))
