#!/usr/bin/node
const args = process.argv;

if (args.length - 2 <= 1) {
  console.log(0);
} else {
  const intArgs = args.slice(2).map(arg => parseInt(arg));
  const sortedInts = intArgs.sort((a, b) => b - a);
  const secondLargest = sortedInts[1];
  console.log(secondLargest);
}
