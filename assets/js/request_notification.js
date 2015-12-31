var old_title = document.title

$(document).ready(function() {
  var baseUrl = $('.js-requests').data('notification-url')
  setInterval(function() {
    $.ajax({
      url: '/requests/',
      dataType: 'html',
      success: function(htmldata) {
        $.ajax({
          url: baseUrl,
          dataType: 'json',
          success: function(data) {
            if (document.hasFocus()) {
              document.title = old_title;
              $('.js-requests').html($(htmldata).find('.js-requests'))
              baseUrl = $(htmldata).find('.js-requests').data('notification-url');
            }
            else {
              if (data.count != 0) {
                document.title = '(' + data.count + ') ' + old_title;
              }
            }
          }
        });
      }
    })
  }, 1000);
});