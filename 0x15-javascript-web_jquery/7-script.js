const $ = window.$;
const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$(() => {
  $.get(URL, (data) => {
    $('#character').text(data.name);
  });
});
