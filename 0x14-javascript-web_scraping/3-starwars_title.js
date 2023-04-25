#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];

const baseURL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(baseURL, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const parsedBody = JSON.parse(body);
  console.log(parsedBody.title);
});
