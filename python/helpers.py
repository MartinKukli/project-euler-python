import math
from functools import lru_cache


def fib_iter(n):
    fibs = [0, 1]
    for num in range(2, n+1):
        fibs.append(fibs[num-2] + fibs[num-1])
    return fibs[n]


def fibb_nums_gen(limit):
    first, second = 1, 2
    while (first < limit):
        yield first
        first, second = second, first + second


def find_primes(n):
    limit = upper_bound_for_nth_prime(n)
    nums = [True for i in range(limit+1)]
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False


def upper_bound_for_nth_prime(n):
    return 100 if n < 6 else ceil(n * (log(n) + log(log(n))))


def divSum(num, result=0, i=2):
    while i <= (math.sqrt(num)):
        if (num % i == 0):
            if (i == (num // i)):
                result = result + i
            else:
                result = result + (i + num//i)
        i = i + 1
    return (result + 1)
