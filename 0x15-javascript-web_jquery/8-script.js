//  fetches and lists the title for all movies by using this URL
const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(URL, function (data) {
  const results = data.results;
  $.each(results, function (key, value) {
    $('#list_movies').append('<li>' + value.title + '</li>');
  });
});
