from helpers import find_primes, upper_bound_for_nth_prime


def find_nth_prime(limit):
    return list(find_primes(limit))[limit - 1]


print(True if find_nth_prime(10001) == 104743 else False)
