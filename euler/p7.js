/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

'use strict';

var a1000th = 7919;

var primeNumbers = [2,3,5,7,11];

var index = 13;

while(primeNumbers.length != 10001) {
  let isPrime = true;
  for(let i = 0; i < primeNumbers.length; i++) {
    if(index%primeNumbers[i]==0) {
      isPrime = false;
      break;
    }
  }

  if(isPrime) {
    primeNumbers.push(index);
  }

  index += 2;
}

console.log(primeNumbers[primeNumbers.length-1]);
