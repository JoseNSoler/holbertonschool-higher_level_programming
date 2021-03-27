#!/usr/bin/node
// New instance square with print in C...

class Square extends require('./5-square.js') {
  charPrint (c) {
    const status = Boolean(c === undefined);
    if (status) super.print();
    if (!status) for (let x = 0; x < this.height; x++) console.log(c.repeat(this.width));
  }
}

module.exports = Square;
