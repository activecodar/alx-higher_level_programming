#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const parsedBody = JSON.parse(body);
  const characterUrls = parsedBody.characters;

  characterUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
