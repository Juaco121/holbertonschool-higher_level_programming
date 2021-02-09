#!/usr/bin/node
// Class for rectangle with a constructor that initializes two instance
// attributes and a print function

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || h <= 0) && w && h) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
