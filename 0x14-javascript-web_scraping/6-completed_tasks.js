#!/usr/bin/node
// Computes the number of tasks completed by user id from
// jsonplaceholder.typicode.com API

const request = require('request');
const urlApi = process.argv[2];

request(urlApi, function (error, response, body) {
  if (error) {
    console.log(error); // Print the error if one occurred
  } else {
    const jsonObj = JSON.parse(body);
    const newDict = {};
    let key = '';

    for (let i = 0; i < jsonObj.length; i++) {
      key = jsonObj[i].userId.toString();
      if (!newDict[key] && jsonObj[i].completed) {
        newDict[key] = 1;
      } else if (jsonObj[i].completed) {
        newDict[key]++;
      }
    }

    console.log(newDict);
  }
});
