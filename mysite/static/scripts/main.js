require(['jquery'], function($) {

    $('#btn-login').on('click',function(){

        var username = $('#login-username').val()
        var password = $('#login-password').val()

        $.ajax({
            type: 'POST',
            url: '/login',
            data: JSON.stringify({
                "username" : username,
                "password" : password
            }),
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function (data) {
                // redirect to URL provided as result
                window.location = "/admin"
            },
            error: function (jqXHR, textStatus, errorThrown) {
                // TODO show error message (has to be localized)
            }
        });


    });

});