/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

'use strict';

// from a list of numbers from 1 to 20, delete all that can be obtained with smaller multiplicaitons
var divisors = [2,3,4,5,7,6,11,13,17,19];

console.log(divisors.reduce(
  function(a,b) {
    return a*b;
  }
));
