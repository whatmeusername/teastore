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


let time = $('.btn-email').attr('data-time')

document.addEventListener('DOMContentLoaded', function() {
    CountDown()

})


function CountDown(){
    $('.btn-email').html(`Повторная отправка ссылки будет доступна через ${time} секунд`)
    if(time > 0){
        time -= 1
        setTimeout(function(){CountDown()}, 1000)
    }
    if(time == 0){
        $('.btn-email').html('Повторно отпраить ссылку на почту')
    }
}

$('.btn-email').on('click', function(){
    if (time == 0 ){
        $.ajax({
            url: window.location.href,
            data: {'resend': true},
            method: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            
            success: function(data){
                time = data.timer || 60
                $('.success-text').html(data.message)
                CountDown()

                setTimeout(function(){
                    $('.success-text').html('')
                }, 15000)

            }

        })
    }

})