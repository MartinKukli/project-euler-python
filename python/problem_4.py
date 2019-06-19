def largest_palindrome_product(largest_palindrome=0):
    digits_products = (x * y for x in range(900, 1000)
                       for y in range(900, 1000))
    for product in digits_products:
        if product == int(str(product)[::-1]) and product > largest_palindrome:
            largest_palindrome = product
    return largest_palindrome


answer = 906609
print(True if largest_palindrome_product() == answer else False)
