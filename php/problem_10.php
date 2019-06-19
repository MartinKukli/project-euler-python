<?php
include "helpers.php";

function summation_of_primes($limit=2000000, $result=0)
{
  $primes_generator = find_primes($limit);
  $primes = [];
  foreach ($primes_generator as $prime) {
    if ($prime < $limit) {
      $primes[] = $prime;
    }
  }
  return array_sum($primes);
}

summation_of_primes();