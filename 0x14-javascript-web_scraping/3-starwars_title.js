#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number
// matches the given integer

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, reply, body) {
  if (err) throw err;
  const content = JSON.parse(body);
  console.log(content.title);
});
