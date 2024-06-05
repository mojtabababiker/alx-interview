#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/';

// return a Promis that requesting the provided url
function fetch (url) {
  // fetch the url and resolve the parsed json object of the
  // response, or reject with the error of the request
  return new Promise((resolve, reject) => {
    request.get(url, (err, response, body) => {
      if (err) {
        reject(err);
      }
      resolve(JSON.parse(body));
    });
  });
}

async function printFilmChars (filmId) {
  try {
    const film = await fetch(`${url}films/${filmId}`);
    const charactersUrl = film['characters'];
    for (const characterUrl of charactersUrl) {
      const character = await fetch(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
  }
}

if (process.argv.length < 3) {
  console.log('Usage: startwars_charcters <film_id>');
} else {
  printFilmChars(process.argv[2]);
}
