sum_of_squares = sum(x ** 2 for x in range(1, 101))
square_of_sum = sum(x for x in range(1, 101)) ** 2
sum_square_difference = square_of_sum - sum_of_squares

print(True if sum_square_difference == 25164150 else False)
