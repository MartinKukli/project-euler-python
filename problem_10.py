from math import log, ceil


def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False
    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False


def upper_bound_for_nth_prime(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def solution_10():
    limit = 2000000
    primes = list(find_primes(upper_bound_for_nth_prime(limit)))
    result = 0

    for prime in primes:
      if prime < limit:
        result += prime
      else:
        break

    return result


print(True if solution_10() == 142913828922 else False)
