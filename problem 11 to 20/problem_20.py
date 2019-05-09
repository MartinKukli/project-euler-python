import math

factorial_digits_sum = sum([int(char) for char in str(math.factorial(100))])

print(True if factorial_digits_sum == 648 else False)
