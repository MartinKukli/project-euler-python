def solution_3(number = 600851475143, prime = 2):
    while (prime ** 2 <= number):
        if (number % prime == 0):
            number //= prime
        else:
            prime += 2 if prime > 2 else 1
    return number


print(True if solution_3() == 6857 else False)
