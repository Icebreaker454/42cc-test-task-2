function cleanErrors() {
    $('.form-group').each(function() {
        $(this).removeClass('has-error');
    });
    $('.help-block').each(function() {
        $(this).remove();
    })
}

function showErrors(errors) {
    for (var field in errors) {
        $('#div_id_' + field).addClass('has-error').append(
          '<p class="help-block"><strong>' + errors[field] + '</strong></p>'
        )
    }
}

function initForm() {
    $('.person-edit-form').ajaxForm({
        dataType: 'json',
        beforeSubmit: function () {
            if($('#photo-clear_id').is(':checked')) {
                $('form .clearablefileinput').clearFields();
            }
            $('input').attr("disabled", "disabled");
            $('textarea').attr("disabled", "disabled");
            $('.loader').show();
        },
        success: function (data, status) {
            if (data.status == 'success') {
                cleanErrors();
                $('#warning').hide();
                $('#message').show();
                $('#message-text').text(data.message);
            }
            else if (data.status == 'error') {
                showErrors(data.errors)
                $('#message').hide();
                $('#warning').show();
                $('#warning-text').text(data.message);
            }

            $('.loader').hide();
            $('input').removeAttr("disabled");
            $('textarea').removeAttr("disabled");
        }
    });
    return false;
}

function initDateField() {
   $('input[name="birth_date"]').datepicker({
       language: 'en',
       dateFormat: 'yyyy-mm-dd'
     });
    return false;
}

$(document).ready(function () {
    initForm();
    initDateField();
});
