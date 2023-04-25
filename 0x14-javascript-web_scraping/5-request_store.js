#!/usr/bin/node

const request = require('request');
const baseURL = process.argv[2];
const pathToFile = process.argv[3];

request(baseURL, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const parsedBody = JSON.parse(body);
  const results = parsedBody.results;
  let counter = 0;
  const charReferenceUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  for (let i = 0; i < results.length; i++) {
    const { characters: charactersArray } = results[i];
    if (charactersArray.includes(charReferenceUrl)) {
      counter += 1;
    }
  }
  console.log(counter);
});
