#!/usr/bin/node
const args = process.argv;

if (args.length - 2 <= 1) {
  console.log(0);
} else {
  const valsArr = [];
  args.slice(2).forEach(element => {
    valsArr.push(parseInt(element));
  });
  valsArr.sort().reverse();
  console.log(valsArr[1]);
}
