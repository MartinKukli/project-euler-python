class Memoize(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        ret = self.func(*args)
        self.cache[args] = ret
        return ret


@Memoize
def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)


def thousand_digit_fib(index=0):
    while True:
        index += 2
        if len(str(fib(index))) == 1000:
            return index


print(True if thousand_digit_fib() == 4782 else False)
