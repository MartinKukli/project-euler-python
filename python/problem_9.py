def special_pythagorean_triplet(input=1000):
    for a in range(1, input):
        for b in range(1, input-a):
            c = input-a-b
            if a**2+b**2 == c**2:
                return a*b*c


answer = 31875000
print(True if special_pythagorean_triplet() == answer else False)
