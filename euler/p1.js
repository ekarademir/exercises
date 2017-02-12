/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

'use strict';

const N = 1000;
var sum = 8;

for(let i = 6; i < N; i++) {
  if(i%3 == 0 || i%5 == 0) {
    // console.log(i);
    sum = sum + i;
  }
}

console.log(sum);