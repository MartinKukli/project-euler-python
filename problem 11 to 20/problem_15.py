import math


def lattice_paths(x=1):
    return math.factorial(x*2) // (math.factorial(x)**2)


print(lattice_paths(20))
