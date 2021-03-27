#!/usr/bin/node
// New instance square with print in C...

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor(size){
    super(size, size);
  }

  charPrint(c){
    if (c === undefined) c = 'x'
    super.print(c);
  }
}

module.exports = Square;
