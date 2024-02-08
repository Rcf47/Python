import datetime

days, seconds = int(input()), int(input())


def shift_time(days: int, seconds: int):
    base_time = datetime.datetime(2023, 1, 1, 12, 30, 0)
    shifted_time = base_time + datetime.timedelta(days=days, seconds=seconds)
    shifted_day = shifted_time.day
    shifted_second = shifted_time.second
    return shifted_day, shifted_second


print(shift_time(days, seconds))
