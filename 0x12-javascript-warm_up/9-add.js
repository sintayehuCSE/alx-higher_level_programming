#!/usr/bin/node
const argOne = Number(process.argv[2]);
const argTwo = Number(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(argOne, argTwo);
