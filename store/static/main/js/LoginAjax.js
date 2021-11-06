
//-------------DJANGO CSRF_TOKEN---------------//
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
//-------------DJANGO CSRF_TOKEN--------------//


let form
let field1
let field2


document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#submit-btn').addEventListener('click', function(e) {

        e.preventDefault();

        form = $('#Login-form').serialize();
        field1 = $('#form-field-1');
        field2 = $('#form-field-2');

        if(field1.val() == ''){
            $('#email-field-error').html('Поле не должно быть пустым');
            field1.css({'border': '1px solid rgb(150, 55, 55)'});
        }

        if(field2.val() == ''){
            $('#password-field-error').html('Поле не должно быть пустым');
            field2.css({'border': '1px solid rgb(150, 55, 55'});
        }

        if(field1.val() != '' & field2.val() != ''){
            LOGIN_AJAX(form);

            field1.css({'border': '0px solid'});
            $('#email-field-error').html();

            field2.css({'border': '0px solid'});
            $('#password-field-error').html();
            
        }


    })
})



function LOGIN_AJAX(form){
    $.ajax({
        url: '/user/login/auth/',
        data: form,
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},

        success: function(res){
            field1.css({'border': '1px solid rgb(150, 55, 55)'});
            field2.css({'border': '1px solid rgb(150, 55, 55)'});
            if(res.message){
                $('#email-field-error').html(res.message);
                field1.css({'border': '1px solid rgb(150, 55, 55)'});
                field2.css({'border': '1px solid rgb(150, 55, 55)'});
            }
            if (res.status == '1'){
                window.location.href = '/'
            }
        }
    })
}