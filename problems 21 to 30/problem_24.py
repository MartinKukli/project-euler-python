from itertools import permutations


millionth_perm = "".join(list(permutations("0123456789", 10))[999999])
print(True if millionth_perm == "2783915460" else False)
