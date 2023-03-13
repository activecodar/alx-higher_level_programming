#!/usr/bin/node
const args = process.argv;

if (isNaN(parseInt(args[2]))) {
  console.log('Missing size');
} else {
  for (let index = 0; index < parseInt(args[2]); index++) {
    console.log('X'.repeat(args[2]));
  }
}
