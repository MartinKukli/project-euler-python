cache = {}


def collatz_sequence(n):
    seq_len = 1

    while n > 1:
        if n % 2 == 0:
            if n in cache:
                n = cache[n]
            else:
                cache[n] = n // 2
                n = n // 2
            seq_len += 1
        else:
            if n in cache:
                n = cache[n]
            else:
                cache[n] = 3*n + 1
                n = 3*n + 1
            seq_len += 1

    return seq_len


def gen_col_seq(index=1000000, longest_seq_num=-1, longest_seq_len=-1):
    while index != 0:
        index -= 1
        seq_len = collatz_sequence(index)
        if longest_seq_len < seq_len:
            longest_seq_num = index
            longest_seq_len = seq_len

    return (longest_seq_num, longest_seq_len)


answer = (837799, 525)
print(True if gen_col_seq() == answer else False)
