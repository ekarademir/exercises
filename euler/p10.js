/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

'use strict';

// from problem 7
var primeNumbers = [2,3,5];

var index = 7;

var sum = 2+3+5;

while(index<2000000) {
  let isPrime = true;
  for(let i = 0; i < primeNumbers.length; i++) {
    if(index%primeNumbers[i]==0) {
      isPrime = false;
      break;
    }
  }

  if(isPrime) {
    primeNumbers.push(index);
    sum += index;
  }

  index += 2;
}

console.log(sum);
