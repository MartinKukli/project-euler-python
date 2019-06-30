<?php
// What is the largest prime factor of the number 600851475143?
function largest_prime_factor($number = 600851475143, $prime = 2)
{
  while ($prime ** 2 <= $number) {
    ($number % $prime == 0) ? ($number /= $prime) : ($prime += ($prime > 2 ? 2 : 1));
  }

  return $number;
}

$anwser = 6857;
echo largest_prime_factor() == $anwser ? "true" : "false";
