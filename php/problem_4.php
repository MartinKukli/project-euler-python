<?php
function reverse_number($number)
{
    // int -> string -> reverse -> int
    $num = (string) $number;
    $revstr = strrev($num);
    $reverse = (int) $revstr;
    
    return $reverse; 
}

function largest_palindrome_product($largest_palindrome=0)
{
    $digits_product = [];
    $loop_range = range(900, 999);

    // generate products with 3-digit numbers
    foreach ($loop_range as $num_one) {
        foreach ($loop_range as $num_two) {
            $digits_product[] = $num_one * $num_two;
        }
    }

    // checks every generated product
    foreach ($digits_product as $number) {
        $reversed_number = reverse_number($number);

        if ($number == $reversed_number and $number > $largest_palindrome) {
            $largest_palindrome = $number;
        }
    }

    return reverse_number($largest_palindrome);
}

$anwser = 906609;
echo largest_palindrome_product() == $anwser ? true : false;
