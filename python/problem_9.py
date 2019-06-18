def special_pythagorean_triplet(input):
    for a in range(1, input):
        for b in range(1, input-a):
            c = input-a-b
            if a**2+b**2 == c**2:
                return a*b*c


print(True if special_pythagorean_triplet(1000) == 31875000 else False)
