#!/usr/bin/node
let x = Number(process.argv[2]);
if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (; x > 0; x--) {
    console.log('C is fun');
  }
}
