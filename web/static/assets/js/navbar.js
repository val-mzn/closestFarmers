$(window).scroll(function() {
    if ($(document).scrollTop() > 100) {
      $('.navbar').addClass('navbar-color-changed');
    } else {
      $('.navbar').removeClass('navbar-color-changed');
    }
  });
