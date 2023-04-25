#!/usr/bin/node
const request = require('request');

const baseUrl = process.argv[2];

request(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }

  const parsedBody = JSON.parse(body);
  const completedTodoObject = {};

  parsedBody.forEach((todo) => {
    if (todo.completed) {
      completedTodoObject[todo.userId] = (completedTodoObject[todo.userId] || 0) + 1;
    }
  });

  console.log(completedTodoObject);
});
