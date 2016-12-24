/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

'use strict';

var sum = 1000;

for(let a = 1; a<=332; a++) {
  for(let b = 2; b<=499; b++) {
    for(let c = 3; c<=997; c++){
      // console.log(a + " * " + b + " * " + c + " = " + (a*b*c));
      if(a+b+c != 1000) {
        continue;
      }else if(a>b || b>c || a>c){
        continue;
      }else{
        if(a*a+b*b == c*c) {
          console.log(a + " * " + b + " * " + c + " = " + (a*b*c));
          break;
        }
      }
    }
  }
}
