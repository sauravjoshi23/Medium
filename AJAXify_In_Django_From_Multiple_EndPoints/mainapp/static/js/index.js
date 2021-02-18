// Form AJAX
$('#form').on('submit', function(e){
  e.preventDefault();
  $.ajax({
       type : "POST",
       url: "/form_ajax/",
       data: {
        firstname : $('#firstname').val(),
        lastname : $('#lastname').val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        dataType: "json",
       },

       success: function(data){
          $('#output1').html(data.msg)
          //call message ajax endpoint
          message_ajax(data.firstname, data.lastname)
       },
       error: function(errorMessage) {
            console.log(errorMessage)
       }
   });
});

// Message AJAX
function message_ajax(firstname, lastname){
    $.ajax({
       type : "POST",
       url: "/message_ajax/",
       data: {
        firstname : firstname,
        lastname : lastname,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        dataType: "json",
       },
       success: function(data){
          $('#output2').html(data)
       },
       error: function(errorMessage) {
            console.log(errorMessage)
       }
    });
}
