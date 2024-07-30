#!/usr/bin/node
// prints characters of Star Wars movie in right order

const request = require('request-promise');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function getCharacterNames(urls) {
  for (const url of urls) {
    try {
      const body = await request(url);
      const character = JSON.parse(body);
      console.log(character.name);
    } catch (error) {
      console.log(error);
    }
  }
}

request(url)
  .then(body => {
    const content = JSON.parse(body);
    return content.characters;
  })
  .then(getCharacterNames)
  .catch(error => {
    console.log(error);
  });
