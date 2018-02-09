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



