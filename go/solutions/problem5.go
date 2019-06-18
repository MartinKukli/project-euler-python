package solutions

// Solution5 => void -> string
func Solution5() string {
	var result int
	number := 10
	runLoop := true
	for runLoop {
		if isDivisible(number) {
			result = number
			runLoop = false
		}
		number++
	}
	if result == 232792560 {
		return "problem 5 solved"
	}
	return "problem 5 not solved"
}

func isDivisible(checkThis int) bool {
	for index := 11; index < 21; index++ {
		if checkThis%index != 0 {
			return false
		}
	}
	return true
}
