/*
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

'use strict';

var range = [];

for (let i = 1; i <= 100; i++)
  range.push(i);

var sumsq = range.map(function(a){
  return a*a;
}).reduce(function(a,b){
  return a+b;
});

var sqsum = range.reduce(function(a,b){
  return a+b;
});

sqsum *= sqsum;

console.log(sqsum-sumsq);
