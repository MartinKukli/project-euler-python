package solutions

// Solution7 => void -> string
func Solution7() string {
	primesIndex := 1
	number := 1
	for primesIndex < 10001 {
		number = number + 2
		if isPrime(number) {
			primesIndex++
		}
	}
	if number == 104743 {
		return "problem 7 solved"
	}
	return "problem 7 not solved"
}

func isPrime(input int) bool {
	if input <= 1 {
		return false
	}
	if input == 2 {
		return true
	}
	if input%2 == 0 {
		return false
	}
	counter := 3
	for counter*counter <= input {
		if input%counter == 0 {
			return false
		}
		counter += 2
	}
	return true
}
