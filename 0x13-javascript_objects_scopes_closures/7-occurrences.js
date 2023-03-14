#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let index = 0; index < list.length; index++) {
    const element = list[index];
    if (searchElement === element) {
      count += 1;
    }
  }
  return count;
};
