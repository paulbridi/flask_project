
$(document).ready(function() {
  $('#text-form').submit(function(event) {
    event.preventDefault();
    var input_text = $('#text-input-string').val();
    $.ajax({
      type: 'POST',
      url: '/text_output/',
      data: {input_text: input_text},
      success: function(result) {
        $('#text_output').html(result);
      }
    });
  });
});
