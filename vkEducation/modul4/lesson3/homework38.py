import datetime

string_datetime = input()


def parse_time(s):
    parsed_time = datetime.datetime.strptime(s, "%Y %m %d %H %M %S")
    shifted_time = parsed_time + datetime.timedelta(days=1)
    return shifted_time.day


print(parse_time(string_datetime))
