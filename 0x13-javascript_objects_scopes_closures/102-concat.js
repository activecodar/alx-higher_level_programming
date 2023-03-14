#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

function concantFile () {
  const fileCPath = args[args.length - 1];
  const fileBPath = args[args.length - 2];
  const fileAPath = args[args.length - 3];
  const dataArr = [];
  const filePathArr = [fileAPath, fileBPath];

  function readFiles () {
    for (let index = 0; index < filePathArr.length; index++) {
      const path = filePathArr[index];
      const data = fs.readFileSync(path, 'utf8');
      dataArr.push(data);
    }
  }

  function writeFile () {
    for (let index = 0; index < dataArr.length; index++) {
      const content = `${dataArr[index]}\n`;
      fs.writeFileSync(fileCPath, content, { flag: 'a+' });
    }
  }

  readFiles();
  writeFile();
}

concantFile();
