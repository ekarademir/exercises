/*
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
*/

'use strict';

var f1 = 1, f2 = 2;

const TOP = 3999999;

var evensum = 2;

while(f2<TOP) {
  let t = f1 + f2;
  if(t%2 === 0) {
    evensum += t;
  }
  // console.log(t);
  f1 = f2;
  f2 = t;
}

console.log(evensum);
