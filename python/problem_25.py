from helpers import fib_rec

def thousand_digit_fib(index=0, length=1000):
    while True:
        index += 2
        if len(str(fib_rec(index))) == length:
            return index

answer = 4782
print(True if thousand_digit_fib() == answer else False)
