

window.onload = init;
function init(){
    let status = 'login';
    const register  = document.querySelector('.register');
    const login = document.querySelector('.login');
    const registerFields = document.querySelector(".register-fields");
    const loginFields = document.querySelector(".login-fields");
    function show_register(){
        registerFields.classList.remove("register-fields")
        registerFields.classList.add("register-fields-reveal");
        loginFields.classList.add('hide');
    }
        
    function show_login(){
        registerFields.classList.remove("register-fields-reveal");
        registerFields.classList.add('register-fields')
        loginFields.classList.remove('hide');
    }

    

    register.addEventListener("click", show_register, false);
    login.addEventListener("click", show_login, false);



}


