package solutions

// Problem2 => nil -> bool
func Problem2() bool {
	limit := 4000000
	answer := 4613732
	firstNum := 1
	secondNum := 2
	result := 2

	for nextNum := 3; nextNum < limit; nextNum = firstNum + secondNum {
		if nextNum%2 == 0 {
			result += nextNum
		}
		firstNum, secondNum = secondNum, nextNum
	}

	return result == answer
}
