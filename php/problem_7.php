<?php
include "helpers.php";

function find_nth_prime($limit = 1001)
{
  $primes = find_primes($limit);
  foreach ($primes as $key => $prime) {
    if ($key === $limit) {
      return $prime;
    }
  }
}

find_nth_prime();