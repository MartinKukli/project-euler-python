from helpers import divSum

# https://www.geeksforgeeks.org/sum-of-all-proper-divisors-of-a-natural-number/
def amicable_nums_sum(limit=10000, result = 0):
    for num in range(1, limit):
        first_sum = divSum(num)
        second_sum = divSum(first_sum)
        if num == second_sum and first_sum != second_sum:
            result += num
    return result


answer = 31626
print(True if amicable_nums_sum() == answer else False)
