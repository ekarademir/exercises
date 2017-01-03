/*
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
*/

'use strict';

/*
for nxn lattice we have n down moves and n left moves
so number of distict ways wouldbe permutation of these
moves

number of unique ways = (n^2)!/n!/n!

*/
function factorial(n) {
  let f = 1;
  for(let i = 1; i <= n; i++)
    f *= i;
  return f;
}

console.log(factorial(40)/factorial(20)/factorial(20));
