#!/usr/bin/node

const request = require('request');
const baseURL = process.argv[2];

request(baseURL, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const parsedBody = JSON.parse(body);
  const results = parsedBody.results;
  let counter = 0;
  for (let i = 0; i < results.length; i++) {
    const { characters: charactersArray } = results[i];
    for (let j = 0; j < charactersArray.length; j++) {
      if (charactersArray[j].endsWith('/18/')) {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
