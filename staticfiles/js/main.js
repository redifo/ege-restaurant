function switchForm(form) {
    if(form === 'login') {
        $('#login-form').show();
        $('#register-form').hide();
    } else {
        $('#login-form').hide();
        $('#register-form').show();
    }
}
