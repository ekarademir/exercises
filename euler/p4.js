/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

'use strict';

function isPalindrome(a) {
  let b = a+"";
  let l = b.length;
  let lp2 = Math.floor(l/2);

  for(let i = 0; i <= lp2; i++)
    if(b[i]!=b[l-i-1])
      return false;

  return true;
}

function findPalindrome() {
  let biggest = 0;
  for(let n1 = 999; n1>99; n1--) {
    for(let n2 = 999; n2>99; n2--) {
      let t = n1*n2;
      if(isPalindrome(t)) {
        console.log(n1 + " x " + n2 + " = " + n1*n2);
        if(t > biggest) {
          biggest = t;
        }
      }
    }
  }
  return biggest;
}

console.log(findPalindrome());
