let link, elements, CartLenght

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


$(document).ready(function() {
    
    elements = document.querySelectorAll('.cart');
    for(let i = 0; i < elements.length; i++) {
        elements[i].addEventListener('click', GetData, false);
    }
    })


function GetData(){
    link = this.getAttribute('data-link');
    AJAX_CART(link);
}

function RELOAD_ELEM(){

    elements = document.querySelectorAll('.cart');
    for(let i = 0; i < elements.length; i++) {
        elements[i].addEventListener('click', GetData, false);
    }

}


function AJAX_CART(link){

    $.ajax({
       url: link,
       data: null,
       method: 'POST',
       headers: {'X-CSRFToken': csrftoken},

       success: function(res_cart){
            CartLenght = document.querySelector('.cart-total');
            CartLenght.innerHTML = CartLenght.innerHTML.slice(0 , CartLenght.innerHTML.length - 1) + res_cart.len;
       }

    })
}
