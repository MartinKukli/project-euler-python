from helpers import fibb_nums_gen


def even_fibonacci_numbers(limit=4000000):
    return sum(x if x % 2 == 0 else 0 for x in fibb_nums_gen(limit))


print(True if even_fibonacci_numbers() == 4613732 else False)
