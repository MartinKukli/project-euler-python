def calc_day(d, m, y):
    '''
    if month has
      | 31 days, then weekday moves by 3
      | 30 days, then it moves by 2
      | 29 days (feb on leap year), then weekday move by 1
      | 28 days (feb on normal year), then it stays the same
    example 1: Tu 1 Jan 1901 => Fr 1 Feb 1901
    example 2: Fr 1 Feb 1901 => Fr 1 Mar
    '''
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        d += 3
    elif m == 4 or m == 6 or m == 9 or m == 11:
        d += 2
    elif m == 2 and y % 4 == 0:
        d += 1
    elif m == 2 and y % 4 != 0:
        d += 0
    # 1 to 7 == Mon to Sun, -7 keeps it that way
    return d - 7 if d > 7 else d


def date_generator(day=2, month=1, year=1901, to_year=2000):
    while year < to_year + 1:
        yield (day, month, year)
        day = calc_day(day, month, year)
        month = month + 1 if month < 12 else 1
        year = year + 1 if month == 12 else year


def count_sundays(num_of_sundays=0):
    for date in date_generator():
        num_of_sundays = num_of_sundays + 1 if date[0] == 7 else num_of_sundays
    return num_of_sundays

answer = 171
print(True if count_sundays() == answer else False)
