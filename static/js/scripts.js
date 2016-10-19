// Кнопка "НАВЕРХ"

  var top_show = 50; // В каком положении полосы прокрутки начинать показ кнопки "Наверх"
  var delay = 750; // Задержка прокрутки
  $(document).ready(function() {
    $(window).scroll(function () { // При прокрутке попадаем в эту функцию
      /* В зависимости от положения полосы прокрукти и значения top_show, скрываем или открываем кнопку "Наверх" */
      if ($(this).scrollTop() > top_show) 
		  $('#scroll_btn img').fadeIn();
      else $('#scroll_btn img').fadeOut();
    });
    $('#scroll_btn img').click(function () { // При клике по кнопке "Наверх" попадаем в эту функцию
      /* Плавная прокрутка наверх */
      $('html, body').animate({
        scrollTop: 0
      }, delay);
    });
  });
  
  //