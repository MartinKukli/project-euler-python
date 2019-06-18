def check_div(input):
    for i in [11, 13, 14, 16, 17, 18, 19, 20]:
        if input % i != 0:
            return False
    return True


def smallest_multiple():
    number = 20
    while True:
        number += 20
        if (check_div(number)):
            return number


answer = 232792560
print(True if smallest_multiple() == answer else False)
