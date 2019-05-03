def solution_5():
    number = 10
    while True:
        number += 1
        if (number % 11 == 0 and
            number % 12 == 0 and
            number % 13 == 0 and
            number % 14 == 0 and
            number % 15 == 0 and
            number % 16 == 0 and
            number % 17 == 0 and
            number % 18 == 0 and
                number % 19 == 0):
            return number


print(True if solution_5() == 232792560 else False)
