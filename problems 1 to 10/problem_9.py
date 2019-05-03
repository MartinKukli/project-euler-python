def solution_9(input):
    for a in range(1, input, 1):
        for b in range(1, input-a, 1):
            c = input-a-b
            if a**2+b**2 == c**2:
                return a*b*c
    return 0


print(True if solution_9(1000) == 31875000 else False)
