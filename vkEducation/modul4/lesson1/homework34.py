numerator, denominator = int(input()), int(input())


def changed_div(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = denominator
    return result


print(changed_div(numerator, denominator))
