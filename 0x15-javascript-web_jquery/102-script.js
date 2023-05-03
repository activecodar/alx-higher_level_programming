const $ = window.$;
$(document).ready(() => {
  $('#btn_translate').click(() => {
    const language = $('#language_code').val();
    const URL = `https://fourtonfish.com/hellosalut/?lang=${language}`;
    $.get(URL, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
