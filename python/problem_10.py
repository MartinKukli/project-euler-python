from helpers import find_primes


def summation_of_primes(limit=2000000):
    return sum(prime if prime < limit else 0 for prime in list(find_primes(limit)))


answer = 142913828922
print(True if summation_of_primes() == answer else False)
