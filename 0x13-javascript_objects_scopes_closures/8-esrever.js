#!/usr/bin/node
exports.esrever = function (list) {
  const revers = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    revers[j] = list[i]; j++;
  }
  return (revers);
};
