def solution_4():
    largest_palindrome = 0
    for first_num in range(100, 1000):
        for second_num in range(100, 1000):
            product = first_num * second_num
            product_string_form = str(product)
            is_palindrome = True if product_string_form[::1] == product_string_form[::-1] else False
            is_greater_than_largest = True if product > largest_palindrome else False
            if (is_palindrome and is_greater_than_largest):
                largest_palindrome = product
    return largest_palindrome


print(True if solution_4() == 906609 else False)
