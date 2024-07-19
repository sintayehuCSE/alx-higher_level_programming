#!/usr/bin/node
const cmdArg = process.argv;
if (cmdArg.length === 2) {
  console.log('No argument');
} else if (cmdArg.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
