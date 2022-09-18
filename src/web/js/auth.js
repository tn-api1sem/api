let userLogin = function () {
    let email = document.getElementById("email").value;
    let password = document.getElementById("pass").value;
    const params = {
        usuario: email,
        senha: password
    }

    const xml = new XMLHttpRequest();
    xml.onloadend = function () {
        if (xml.status == 200) {
            console.log(xml.response);
            //Redirecionar
            return;
        }
    };

    xml.onerror = function(){
        alert("Usuario/Senha incorretos");
    }

    xml.open("POST", localURL + "/api/v1/auth");
    xml.setRequestHeader('Access-Control-Allow-Origin', '*');
    xml.setRequestHeader('Content-type', 'application/json');
    xml.send(JSON.stringify(params));
};