
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

//-----DELAY------------//
function delay(fn, ms) {
    let timer = 0
    return function(...args) {
      clearTimeout(timer)
      timer = setTimeout(fn.bind(this, ...args), ms || 0)
    }
  }
//----DELAY-------//



let form
let field1
let field2
let field3
let field4
let field5

let FieldValue


document.addEventListener('DOMContentLoaded', function() {


    field1 = $('#form-field-1');
    field2 = $('#form-field-2');
    field3 = $('#form-field-3');
    field4 = $('#form-field-4');
    field5 = $('#form-field-5');


    document.querySelector('#submit-btn').addEventListener('click', function(e) {
        e.preventDefault();
        CollectAndSendData()
    })

    $('.register-form-field').keyup(delay(function(){
        FieldValue = {[$(this).attr('name')]: $(this).val()}

        if (FieldValue != ''){

            if (Object.keys(FieldValue) == 'password_repeat'){
                FieldValue[field4.attr('name')] = field4.val()
            }
            FIELD_VALIDATOR_AJAX(FieldValue)
        }

    }, 500))


})




function REGISTER_AJAX(form){
    $.ajax({
        url: '/user/register/auth/',
        data: form,
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},

        success: function(data){
            SetErrors(data);
            if (data.link){
                window.location.href = data.link
            }       
        }    
    })
}

function FIELD_VALIDATOR_AJAX(field){
    $.ajax({
        url: '/user/register/validator/',
        data: FieldValue,
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},

        success: function(data){
            SetErrors(data);
            }

    })
}




function CollectAndSendData(){

    form = $('#register-form').serialize();


        CheckEmpty()


        if(field1.val() != '' & 
            field2.val() != '' & 
            field3.val() != '' & 
            field4.val() != '' & 
            field5.val() != '')
            {
                REGISTER_AJAX(form);

                field1.css({'border': '0px solid'});
                $('#email-field-error').html('');

                field2.css({'border': '0px solid'});
                $('#FirstName-field-error').html('');

                field3.css({'border': '0px solid'});
                $('#LastName-field-error').html('');

                field4.css({'border': '0px solid'});
                $('#password-field-error').html('');

                field5.css({'border': '0px solid'});
                $('#password_repeat-field-error').html('');
                
            }
}


function CheckEmpty(){

    if(field1.val() == ''){
        $('#email-field-error').html('Поле не должно быть пустым');
        field1.css({'border': '1px solid rgb(150, 55, 55)'});
    }

    if(field2.val() == ''){
        $('#FirstName-field-error').html('Поле не должно быть пустым');
        field2.css({'border': '1px solid rgb(150, 55, 55'});
    }

    if(field3.val() == ''){
        $('#LastName-field-error').html('Поле не должно быть пустым');
        field3.css({'border': '1px solid rgb(150, 55, 55)'});
    }

    if(field4.val() == ''){
        $('#password-field-error').html('Поле не должно быть пустым');
        field4.css({'border': '1px solid rgb(150, 55, 55'});
    }

    if(field5.val() == ''){
        $('#password_repeat-field-error').html('Поле не должно быть пустым');
        field5.css({'border': '1px solid rgb(150, 55, 55'});
    }

}

function SetErrors(data){

    //-----EMAIL------//
    if (data.email && data.email != true){
        $('#email-field-error').html(data.email);
        field1.css({'border': '1px solid rgb(150, 55, 55)'});
    }
    else if(data.email == true){
        field1.css({'border': '1px solid rgb(82, 150, 55)'});
        $('#email-field-error').html('');
    }


    //------FIRSTNAME-----//
    if (data.FirstName && data.FirstName != true){
        $('#FirstName-field-error').html(data.FirstName);
        field2.css({'border': '1px solid rgb(150, 55, 55)'});
    }
    else if(data.FirstName == true) {
        field2.css({'border': '1px solid rgb(82, 150, 55)'});
        $('#FirstName-field-error').html('');
    }

    //----LASTNAME----//
    if (data.LastName && data.LastName != true){
        $('#LastName-field-error').html(data.LastName);
        field3.css({'border': '1px solid rgb(150, 55, 55)'});
    }
    else if(data.LastName == true){
        field3.css({'border': '1px solid rgb(82, 150, 55)'});
        $('#LastName-field-error').html('');
    }

    //----PASSWORD----//
    if (data.password && data.password != true){
        $('#password-field-error').html(data.password);
        field4.css({'border': '1px solid rgb(150, 55, 55)'});
    }
    else if(data.password == true){
        field4.css({'border': '1px solid rgb(82, 150, 55)'});
        $('#password-field-error').html('');
    }

    //----PASSWORD_REPEAT---//
    if (data.password_repeat && data.password_repeat != true){
        $('#password_repeat-field-error').html(data.password_repeat);
        field5.css({'border': '1px solid rgb(150, 55, 55)'});
    }
    else if(data.password_repeat == true){
        field5.css({'border': '1px solid rgb(82, 150, 55)'});
        $('#password_repeat-field-error').html('');
    }

}
