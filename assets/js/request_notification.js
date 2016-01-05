var old_title = document.title

function setLastRequest(Url, newRequest) {
  var array = Url.split('/');
  var number = array[array.length - 1];
  return Url.replace(number, newRequest);
}

function formatDate(date) {
  return date.getUTCFullYear() + '-' + 
    ((date.getUTCMonth() < 9) ? ('0' + (date.getUTCMonth() + 1)) : date.getUTCMonth() + 1 ) + '-' +
    ((date.getUTCDate() < 10) ? ('0' + date.getUTCDate()) : date.getUTCDate()) + ' ' +
    date.getUTCHours() + ':' +
    ((date.getUTCMinutes() < 10) ? ('0' + date.getUTCMinutes()) : date.getUTCMinutes()) + ':' +
    ((date.getUTCSeconds() < 10) ? ('0' + date.getUTCSeconds()) : date.getUTCSeconds())
}

$(document).ready(function() {
  var baseUrl = $('.js-requests').data('notification-url');
  var window_focus = true;

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
          var queryset = $.parseJSON(data.queryset);
          baseUrl = setLastRequest(baseUrl, queryset[0].pk);
          var tableHtml;

          for (var i = 0; i < queryset.length; i++) {
            tableHtml = tableHtml +
              '<tr>' +
                '<td>' + (i + 1) + '</td>' +
                '<td>' + queryset[i].fields.path + '</td>' +
                '<td>' + formatDate(new Date(queryset[i].fields.time)) + '</td>' +
                '<td>' + queryset[i].fields.user_agent + '</td>' +
                '<td>' + queryset[i].fields.method + '</td>' +
                '<td>' + (queryset[i].fields.is_secure ? '+' : '-') + '</td>' +
                '<td>' + (queryset[i].fields.is_ajax ? '+' : '-') + '</td>' +
              '</tr>'
          }
          $('.js-requests tbody').html(tableHtml);

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