<?php
function multiples_of_3_and_5($limit = 1000)
{
    $ok_nums = [3, 5];

    foreach (range(6, $limit - 1) as $num) {
        if ($num % 3 == 0 or $num % 5 == 0) {
            $ok_nums[] = $num;
        }
    }

    return array_sum($ok_nums);
}

$answer = 233168;
echo multiples_of_3_and_5() == $answer ? "true" : "false";
