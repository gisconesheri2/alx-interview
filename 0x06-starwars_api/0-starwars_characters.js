const request = require('request');

if (process.argv.length !== 3) {
  throw new Error('need one argument');
}

const num = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${num}/`;

function getCharacter (url) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(request(url, function (error, response, body) {
        if (error) {
          return;
        }
        const characterJson = JSON.parse(body);
        console.log(characterJson.name);
      }));
    }, 500);
  });
}

request(url, async function (error, responce, body) {
  if (error) {
    return;
  }
  const jsonBody = JSON.parse(body);
  const charactersUrls = jsonBody.characters;

  for (const url of charactersUrls) {
    await getCharacter(url);
  }
});
