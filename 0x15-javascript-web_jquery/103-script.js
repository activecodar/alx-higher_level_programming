const $ = window.$;
$(document).ready(() => {
  const url = 'https://www.fourtonfish.com/hellosalut/';
  $('#btn_translate, #language_code').click(() => {
    const langCode = $('#language_code').val();
    if (langCode !== '') {
      $.getJSON(url, { lang: langCode }, data => {
        $('#hello').text(data.hello);
      });
    }
  });
  $('#language_code').keypress(event => {
    if (event.keyCode === 13) {
      event.preventDefault();
      $('#btn_translate').click();
    }
  });
});
