const $ = window.$;
const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(() => {
  $.get(URL, (data) => {
    $.each(data.results, (index, film) => {
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  });
});
