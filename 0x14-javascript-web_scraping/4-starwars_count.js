#!/usr/bin/node
// Prints the number of movies where "Wedge Antilles" is present

const request = require('request');
const urlApi = process.argv[2];

request(urlApi, function (error, response, body) {
  if (error) {
    console.log(error); // Print the error if one occurred
  } else {
    const jsonObj = JSON.parse(body).results;
    let count = 0;
    let charList;
    for (let i = 0; i < jsonObj.length; i++) {
      charList = jsonObj[i].characters;
      charList.forEach(element => {
        if (element.search('/18/') > 0) {
          count += 1;
        }
      });
    }
    console.log(count);
  }
});
