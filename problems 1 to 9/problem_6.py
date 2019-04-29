sumOfSquares = sum([x ** 2 for x in range(1, 101)])
squareOfSum = sum([x for x in range(1, 101)]) ** 2

print(True if (squareOfSum - sumOfSquares == 25164150) else False)
