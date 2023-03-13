#!/usr/bin/node
const args = process.argv;

function factorial (fact) {
  const factInt = fact === undefined ? null : parseInt(fact);
  if (isNaN(factInt)) {
    return 1;
  } else {
    if (factInt <= 1) {
      return 1;
    } else {
      return factInt * factorial(factInt - 1);
    }
  }
}

console.log(factorial(args[2]));
