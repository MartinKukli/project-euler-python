<?php
function sum_of_squares($result = 0)
{
  foreach (range(1, 101) as $num) {
    $result += $num ** 2;
  }
  return $result;
}

function square_of_sum($result = 0)
{
  foreach (range(1, 101) as $num) {
    $result += $num;
  }
  return $result ** 2;
}

$sum_square_difference = square_of_sum() - sum_of_squares();

$answer = 25164150;
echo $sum_square_difference." === ".$answer;