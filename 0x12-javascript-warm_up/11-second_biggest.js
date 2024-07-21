#!/usr/bin/node
let arr = process.argv.map((n) => Number(n));
arr = arr.filter((n) => !isNaN(n));
const len = arr.length;
if (len === 0 || len === 1) {
  console.log(0);
} else {
  let secBig;
  let count = 0;
  let iter = 0;
  while (iter < len) {
    secBig = arr[iter];
    for (let i = 0; i < len; i++) {
      if (arr[i] > secBig) count++;
      if (count > 1) break;
    }
    if (count === 1) {
      console.log(secBig);
      break;
    }
    count = 0;
    iter++;
  }
}
