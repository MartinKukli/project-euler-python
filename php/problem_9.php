<?php
function special_pythagorean_triplet($input)
{
  foreach (range(1, $input) as $a) {
    foreach (range(1, ($input - $a)) as $b) {
      $c = $input - $a - $b;
      if ($a ** 2 + $b ** 2 === $c ** 2) {
        return $a * $b * $c;
      }
    }
  }
}

$answer = 31875000;
echo special_pythagorean_triplet(1000) === $answer ? "true" : "false";