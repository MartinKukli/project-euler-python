def solution_4(largest_palindrome=0):
    for first_num in range(900, 1000):
        for second_num in range(900, 1000):
            product = first_num * second_num
            product_reversed = reverse_int(product)

            is_palindrome = True if product == product_reversed else False
            is_greater_than_largest = True if product > largest_palindrome else False

            if (is_palindrome and is_greater_than_largest):
                largest_palindrome = product

    return largest_palindrome


def reverse_int(num):
    new_num = 0
    while num > 0:
        remainder = num % 10
        new_num = new_num * 10 + remainder
        num = int(num / 10)
    return new_num

print(True if solution_4() == 906609 else False)
