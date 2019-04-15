def solution_6_part_1(limit):
    result = 0
    for index in range(1, limit + 1):
        result += index ** 2
    return result


def solution_6_part_2(limit):
    result = 0
    for index in range(1, limit + 1):
        result += index
    return result ** 2


print(True if (solution_6_part_2(100) - solution_6_part_1(100) == 25164150) else False)
