const $ = window.$;
$(document).ready(() => {
  $('#toggle_header').on('click', () => {
    const currentClass = $('header').attr('class');
    if (currentClass === 'green') {
      $('header').removeClass('green').addClass('red');
    } else {
      $('header').removeClass('red').addClass('green');
    }
  });
});
