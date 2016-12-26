/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

'use strict';

var chainlengths = [1];

/* chain is unique. once the chain produces a number on the
chain it'll go down to 1 the same way*/

for(let i  = 2; i < 1000000; i++) {
  let n = i;
  let currentLength = 0;
  while(n > chainlengths.length) {
    if(n%2==0) {
      n = n/2;
      currentLength++;
    } else {
      n = 3*n+1;
      currentLength++;
    }
  }
  currentLength += chainlengths[n-1];
  chainlengths.push(currentLength);
}

var index = -1, max = 0;

for(let i = 0; i<chainlengths.length; i++) {
  if(chainlengths[i] > max) {
    max = chainlengths[i];
    index = i;
  }
}

console.log((index+1) + ': ' + max);
