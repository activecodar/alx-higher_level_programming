#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newArray = list.map((idx, num) => num * idx);
console.log(newArray);
