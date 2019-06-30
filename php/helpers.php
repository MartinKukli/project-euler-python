<?php
function upper_bound_for_nth_prime($n)
{
  return ($n < 6) ? 100 : ceil($n * (log($n) + log(log($n))));
}

function fib($limit)
{
  $cur = 2;
  $prev = 1;

  while ($cur < $limit) {
    yield $cur;

    $temp = $cur;
    $cur = $prev + $cur;
    $prev = $temp;
  }
}

function find_primes($n)
{
  $limit = upper_bound_for_nth_prime($n);
  $nums = array_fill(1, $limit, true);
  $nums[1] = false;
  foreach ($nums as $key => &$value) {
    if ($value) {
      yield $key;
      foreach (range($key * $key, $limit + 1, $key) as $num) {
        $nums[$num] = false;
      }
    }
  }
  unset($value);
}
