const $ = window.$;
const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(() => {
  $.get(URL, (data) => {
    $('#hello').text(data.hello);
  });
});
