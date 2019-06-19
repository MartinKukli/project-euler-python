from helpers import find_primes, upper_bound_for_nth_prime


def summation_of_primes(limit=2000000):
    return sum([prime if prime < limit else 0 for prime in list(find_primes(limit))])


print(True if summation_of_primes() == 142913828922 else False)
