<?php
function smallest_multiple()
{
    $number = 20;

    while (true) {
        $number += 1;

        if ($number % 11 == 0 and
            $number % 12 == 0 and
            $number % 13 == 0 and
            $number % 14 == 0 and
            $number % 15 == 0 and
            $number % 16 == 0 and
            $number % 17 == 0 and
            $number % 18 == 0 and
            $number % 19 == 0) {
            return $number;
        }
    }
}

$answer = 232792560;
echo smallest_multiple() == $answer ? true : false;
