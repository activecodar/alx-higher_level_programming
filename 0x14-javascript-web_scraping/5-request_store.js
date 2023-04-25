#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const baseURL = process.argv[2];
const pathToFile = process.argv[3];

request(baseURL, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  fs.writeFile(pathToFile, body, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
