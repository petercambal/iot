require(['jquery','bootstrap'], function($) {

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

    $('#btn-signup').on('click',function(){

        var username = $('#username').val();
        var password = $('#password').val();
        var repassword = $('#re-password').val();

        if (password != repassword) {
            return false
        }

        console.log(password)
        $.ajax({
            type: 'POST',
            url: '/register',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify({
                "username" : username,
                "password" : password
            }),
            dataType: 'json',
            success: function (data) {
                // redirect to URL provided as result
                window.location = "/login"
            },
            error: function (jqXHR, textStatus, errorThrown) {
                // TODO show error message (has to be localized)
            }
        });
    });

    $('#btn-logout').on('click',function(){

        $.ajax({
            type: 'GET',
            url: '/logout',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function (data) {
                // redirect to URL provided as result
                window.location = "/"
            },
            error: function (jqXHR, textStatus, errorThrown) {
                // TODO show error message (has to be localized)
            }
        });
    });


 $(".menu-toggle").click(function(e) {
            $("#wrapper").toggleClass("toggled");
        });


});