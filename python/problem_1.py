def multiples_of_3_and_5(limit=1000):
    return sum(x if x % 3 == 0 or x % 5 == 0 else 0 for x in range(1, limit))


print(True if multiples_of_3_and_5() == 233168 else False)
