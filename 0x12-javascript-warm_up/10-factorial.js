#!/usr/bin/node
const num = Number(process.argv[2]);
function factorial (num) {
  if (!num) return 1;
  if (num === 0) return 1;
  return (num * factorial(num - 1));
}
console.log(factorial(num));
