#!/usr/bin/node
const args = process.argv;
if ((args.length - 2) < 1) {
  console.log('No argument');
} else if ((args.length - 2) === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
