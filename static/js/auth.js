let userLogin = function () {
    let form = document.getElementById("login-form");
    let email = form.elements.namedItem("email").value;
    let password = form.elements.namedItem("password").value;
    let credentials = "email=" + email + "&password=" + password;
    const params = {
        email: form.elements.namedItem("email").value,
        password: form.elements.namedItem("password").value
    }
    const xml = new XMLHttpRequest();

    xml.onreadystatechange = function () {
        if (xml.status == 200) {
            console.log(xml.response);
        }
    };

    xml.open("POST", "/api/v1/autenticacao");//url para enviar a requisição
    //xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    //xml.send(credentials);
    xml.setRequestHeader('Content-type', 'application/json');
    xml.send(JSON.stringify(params));
};