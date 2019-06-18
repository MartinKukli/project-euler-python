def triangular_number():
    tri_num = 0
    index = 1
    while True:
        yield tri_num + index
        tri_num += index
        index += 1


def factors(n):
    l1, l2 = [], []
    for i in range(1, int(n ** 0.5) + 1):
        q, r = n//i, n % i
        if r == 0:
            l1.append(i)
            l2.append(q)
    if l1[-1] == l2[-1]:
        l1.pop()
    l2.reverse()
    return l1 + l2


def highly_divisible_triangular_number(div_count_limit):
    result = (0, 0)
    for tri_num in triangular_number():
        divisors_count = len(factors(tri_num))
        if divisors_count >= div_count_limit:
            result = (divisors_count, tri_num)
            break
    return result


# returns tuple(factor count, triangular number)
print(highly_divisible_triangular_number(500))
