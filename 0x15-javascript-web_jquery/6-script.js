const $ = window.$;
$(() => {
  $('#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
