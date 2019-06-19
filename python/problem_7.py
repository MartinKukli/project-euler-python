from helpers import find_primes


def find_nth_prime(limit=10001):
    return list(find_primes(limit))[limit - 1]


answer = 104743
print(True if find_nth_prime() == answer else False)
