#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const num = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${num}/`;

  function getCharacter (url) {
    return new Promise((resolve, reject) => {
      request(url, function (error, response, body) {
        if (error) {
          reject(error);
        }
        resolve((JSON.parse(body).name));
      });
    });
  }

  request(url, function (error, responce, body) {
    if (error) {
      console.log(error);
    }
    const jsonBody = JSON.parse(body);
    const charactersUrls = jsonBody.characters;
    const charactersName = charactersUrls.map(getCharacter);

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
