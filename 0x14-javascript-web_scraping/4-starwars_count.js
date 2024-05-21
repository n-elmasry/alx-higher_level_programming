#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    const characters = film.characters;
    if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
