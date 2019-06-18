package solutions

// Solution4 => void -> string
func Solution4() string {
	largestPalindrome := 0
	for firstNum := 999; firstNum >= 900; firstNum-- {
		for secondNum := 999; secondNum >= 900; secondNum-- {
			product := firstNum * secondNum
			productReversed := reverseInt(product)

			if product == productReversed && product > largestPalindrome {
				largestPalindrome = product
			}
		}
	}
	if largestPalindrome == 906609 {
		return "problem 4 solved"
	}
	return "problem 4 not solved"
}

func reverseInt(n int) int {
	newInt := 0
	for n > 0 {
		remainder := n % 10
		newInt *= 10
		newInt += remainder
		n /= 10
	}
	return newInt
}
