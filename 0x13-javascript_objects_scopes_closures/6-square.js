#!/usr/bin/node

const SquareParent = require('./5-square');

module.exports = class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      for (let index = 0; index < this.height; index++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let index = 0; index < this.height; index++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
