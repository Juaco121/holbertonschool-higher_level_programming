#!/usr/bin/node
// Displays the status code of a GET request

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error); // Print the error if one occurred
  } else {
    console.log('code:', response && response.statusCode); // Print the response status code if a response was received
  }
});
