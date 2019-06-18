package solutions

// Problem3 => nil -> bool
func Problem3() bool {
	input := 600851475143
	answer := 6857

	for prime := 2; prime*prime <= input; {
		if input%prime == 0 {
			input /= prime
		}
		if prime > 2 {
			prime += 2
		} else {
			prime++
		}
	}

	return input == answer
}
