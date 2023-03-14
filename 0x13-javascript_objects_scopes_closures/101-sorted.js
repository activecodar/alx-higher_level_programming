#!/usr/bin/node
const dict = require('./101-data').dict;
const newObject = {};

for (const property in dict) {
  const key = dict[property];
  if (newObject[key] === undefined) {
    newObject[key] = [];
    newObject[key].push(property);
  } else {
    newObject[key].push(property);
  }
}

console.log(newObject);
