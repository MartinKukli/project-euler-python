<?php
function largest_prime_factor($number = 600851475143, $prime = 2)
{
    while ($prime ** 2 <= $number) {
        if ($number % $prime == 0) {
            $number /= $prime;
        } else {
            $prime += $prime > 2 ? 2 : 1;
        }
    }

    return $number;
}

$anwser = 6857;
echo largest_prime_factor() == $anwser ? true : false;
