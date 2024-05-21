#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    const characters = film.characters;
    if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/' || 'http://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
