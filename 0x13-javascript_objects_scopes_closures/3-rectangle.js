#!/usr/bin/node
// class Rectangle with restrictions (Only positive numbers) and method print

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) return null;
    this.width = w;
    this.height = h;
  }

  print () {
    let yStr = '';

    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) yStr += 'X';
      console.log(yStr);
      yStr = '';
    }
  }
}

module.exports = Rectangle;
