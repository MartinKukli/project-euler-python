special_pythagorean_triplet = [a*b*(1000-a-b) for a in range(1, 1000)
                               for b in range(1, 1000-a) if a**2+b**2 == (1000-a-b)**2][0]
answer = 31875000
print(True if special_pythagorean_triplet == answer else False)
