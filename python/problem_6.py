sum_square_difference = (sum(x for x in range(1, 101))
                         ** 2) - (sum(x ** 2 for x in range(1, 101)))


answer = 25164150
print(True if sum_square_difference == answer else False)
