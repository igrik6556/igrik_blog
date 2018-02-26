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
  
// Ajaxify PASS_GENERATOR

var csrftoken = $('input[name=csrfmiddlewaretoken]').val();

$('#pass_gen').on('submit', function(event){
    event.preventDefault();
    $.ajax({
        headers: {"X-CSRFToken": csrftoken},
        url : "generate/",
        type : "POST",
        data : {
            up_letters : $('#id_up_letters').prop('checked'),
            low_letters : $('#id_low_letters').prop('checked'),
            digits : $('#id_digits').prop('checked'),
            spec_symbols : $('#id_spec_symbols').prop('checked'),
            user_symbols : $('#id_user_symbols').val(),
            length : $('#id_length').val(),
            number : $('#id_number').val()
        },
        success : function(json) {
            $("#passwords").html('');
            $.each(json.passwords, function(index, value){
                pass = "<li>" + value.replace(new RegExp("<", "g"),'&lt;').replace(new RegExp(">", "g"),'&gt;') + "</li>";
                $("#passwords").append(pass);
            });
        },
        error : function(xhr, errmsg, err) {
            $('#passwords').html("<li class='ajax-error'>Oops! We have encountered an error: " + errmsg + "</li>");
        },
    });
});
