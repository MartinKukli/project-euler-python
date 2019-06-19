from itertools import permutations


millionth_perm = int("".join(list(permutations("0123456789", 10))[999999]))
answer = 2783915460
print(True if millionth_perm == answer else False)
