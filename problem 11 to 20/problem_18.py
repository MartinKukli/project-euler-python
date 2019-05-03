n_tri = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


def max_path_sum():
    # loop through every row before the last row; last row contains paths sums
    for r_index in range(len(n_tri)-1):
        # iterates for count of values in the next row
        r_len = len(n_tri[r_index+1])
        for v_index in range(r_len):
            # first and last value have only one value on top of them
            if v_index == 0:
                n_tri[r_index+1][0] += n_tri[r_index][0]
            elif v_index == r_len-1:
                n_tri[r_index+1][-1] += n_tri[r_index][-1]
            else:
                # compares two value over the next row value
                if n_tri[r_index][v_index-1] > n_tri[r_index][v_index]:
                    n_tri[r_index+1][v_index] += n_tri[r_index][v_index-1]
                else:
                    n_tri[r_index+1][v_index] += n_tri[r_index][v_index]
    # returns max path sum
    return max(n_tri[-1])


print(True if max_path_sum() == 1074 else False)
