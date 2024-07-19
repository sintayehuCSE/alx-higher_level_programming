#!/usr/bin/node
const cmdArg = process.argv;
if (cmdArg[2]) {
  console.log(cmdArg[2]);
} else {
  console.log('No argument');
}
