<?php
function check_div($input)
{
  foreach (array(11, 13, 14, 16, 17, 18, 19, 20) as $i) {
    if ($input % $i != 0) {
      return False;
    }
  }
  return True;
}

function smallest_multiple($number = 20)
{
  while (true) {
    $number += 20;
    if (check_div($number)) {
      return $number;
    }
  }
}

$answer = 232792560;
echo smallest_multiple() == $answer ? "true" : "false";
