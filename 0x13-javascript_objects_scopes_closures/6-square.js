#!/usr/bin/node
const Square5 = require('./5-square');
module.exports = class Square extends Square5 {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let side = '';
        for (let j = 0; j < this.width; j++) {
	  side += c;
        }
        console.log(side);
      }
    } else {
      this.print();
    }
  }
};
