def solution_1(limit):
    return sum([x if x % 3 == 0 or x % 5 == 0 else 0 for x in range(1, limit)])


print(True if solution_1(1000) == 233168 else False)
