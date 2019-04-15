def fibb_gen(limit):
  first, second = 1, 2
  while (first < limit):
    yield first
    first, second = second, first + second

def solution_2_2(limit):
  return sum([x if x % 2 == 0 else 0 for x in fibb_gen(limit)])

print(True if solution_2_2(4000000) == 4613732 else False)