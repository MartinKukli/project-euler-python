import math

# https://www.geeksforgeeks.org/sum-of-all-proper-divisors-of-a-natural-number/


def divSum(num):
    result = 0
    i = 2
    while i <= (math.sqrt(num)):
        if (num % i == 0):
            if (i == (num // i)):
                result = result + i
            else:
                result = result + (i + num//i)
        i = i + 1
    return (result + 1)


def amicable_nums_sum(limit=10000):
    result = 0
    for num in range(1, limit):
        first_sum = divSum(num)
        second_sum = divSum(first_sum)
        if num == second_sum and first_sum != second_sum:
            result += num
    return result


print(True if amicable_nums_sum() == 31626 else False)
