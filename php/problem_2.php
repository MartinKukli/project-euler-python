<?php
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

  function even_fib_nums($limit = 4000000)
  {
    $fibs = fib($limit);
    $even_fibs = [];

    foreach ($fibs as $fib) {
      if ($fib % 2 == 0) {
        $even_fibs[] = $fib;
      }
    }

    return array_sum($even_fibs);
  }

  $answer = 4613732;
  echo even_fib_nums() == $answer ? true : false;
