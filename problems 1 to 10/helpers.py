from math import log, ceil


def fibb_nums_gen(limit):
    first, second = 1, 2
    while (first < limit):
        yield first
        first, second = second, first + second


def find_primes(n):
    limit = upper_bound_for_nth_prime(n)
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False


def upper_bound_for_nth_prime(n):
    return 100 if n < 6 else ceil(n * (log(n) + log(log(n))))
