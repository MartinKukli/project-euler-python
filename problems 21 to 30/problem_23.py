import math


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


def abundant_nums_gen(start=1, limit=28124):
    abundant = []
    for num in range(start, limit):
        div_sum = divSum(num)
        if div_sum > num:
            abundant.append(num)
    return abundant


def abundant_num_sums(limit=28124):
    result = [False] * limit
    abundant_nums = abundant_nums_gen()
    for num_one in range(len(abundant_nums)):
        for num_two in range(len(abundant_nums)):
            if abundant_nums[num_one] + abundant_nums[num_two] < limit:
                result[abundant_nums[num_one] + abundant_nums[num_two]] = True
    return result


def non_abundant_sums(limit=28124):
    result = 0
    abundant_nums = abundant_num_sums()
    for num in range(1, limit):
        if not abundant_nums[num]:
            result += num
    return result


print(True if non_abundant_sums() == 4179871 else False)
