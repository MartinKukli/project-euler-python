import math


def lattice_paths(x=1, y=1):
    return math.factorial(x+y) // (math.factorial(x) * math.factorial(y))


print(lattice_paths(20, 20))
