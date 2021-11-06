document.addEventListener('DOMContentLoaded', function() {
    const user = document.querySelector('.dropdown-user');
    const UserGUI = document.querySelector('.dropdown-content-user')

    user.addEventListener('click', function(){
        UserGUI.classList.toggle('active')
    })
})