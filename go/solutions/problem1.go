package solutions

// Problem1 => nil -> bool
func Problem1() bool {
	limit := 1000
	answer := 233168
	result := 0

	for checkPoint := 0; checkPoint < limit; checkPoint++ {
		if checkPoint%3 == 0 || checkPoint%5 == 0 {
			result += checkPoint
		}
	}

	return result == answer
}
