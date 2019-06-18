from math import ceil, log
from functools import lru_cache


@lru_cache(None)
def fib_rec(n):
    return 1 if n < 2 else fib_rec(n-2) + fib_rec(n-1)


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
