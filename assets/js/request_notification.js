var old_title = document.title

function setLastRequest(Url, newRequest) {
  var array = Url.split('/');
  var number = array[array.length - 1];
  return Url.replace(number, newRequest);
}

$(document).ready(function() {
  var baseUrl = $('.js-requests').data('notification-url');
  var window_focus;

  $(window).focus(function() {
      window_focus = true;
  }).blur(function() {
      window_focus = false;
  });
  setInterval(function() {
    $.ajax({
      url: baseUrl,
      dataType: 'json',
      success: function(data) {
        if (window_focus) {
          document.title = old_title;

          var queryset = JSON.parse(data.queryset);
          console.log(queryset);
/*
          // TODO: TABLE CHANGE
          $('.js-requests tr').each(function(i) {
            if (i < queryset.length) {
              $('td.js-path', this).text(queryset[i].fields.path);
              $('td.js-time', this).text(queryset[i].fields.time);
              $('td.js-useragent', this).text(queryset[i].fields.user_agent);
              $('td.js-method', this).text(queryset[i].fields.method);
              $('td.js-issecure', this).text(queryset[i].fields.is_secure);
              $('td.js-isajax', this).text(queryset[i].fields.is_ajax);
            }
          })
*/
          // TODO: BaseUrl
          baseUrl = setLastRequest(baseUrl, queryset[0].pk);
          console.log(baseUrl)
        }
        else {
          if (data.count != 0) {
            document.title = '(' + data.count + ') ' + old_title;
          }
        }
      }
    });
  }, 1000);
});