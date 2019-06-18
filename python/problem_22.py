def names_scores():
    result = 0
    alphabet_values = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
                       "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    with open("python/names.txt", "r") as f:
        # get names. split by coma, remove "", turn name into list of char
        names = [list(name[1:-1]) for name in f.read().split(",")]
        # sort names, alphabetical order
        names.sort()
        # loop over every "name", replace char with number, sum and mult by index+1
        for index in range(len(names)):
            result += sum([alphabet_values[char]
                           for char in names[index]]) * (index + 1)
    return result


print(True if names_scores() == 871198282 else False)
