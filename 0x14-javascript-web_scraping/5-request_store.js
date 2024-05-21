#!/usr/bin/node
const request = require('request');
const filesys = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    filesys.writeFile(file, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
