package solutions

// Solution6 => void -> string
func Solution6() string {
	calcResult := squareOfSum(100) - sumOfSquares(100)
	if calcResult == 25164150 {
		return "problem 6 solved"
	}
	return "problem 6 not solved"
}

func sumOfSquares(limit int) int {
	result := 0
	for index := 1; index <= limit; index++ {
		result += index * index
	}
	return result
}

func squareOfSum(limit int) int {
	result := 0
	for index := 1; index <= limit; index++ {
		result += index
	}
	return result * result
}
