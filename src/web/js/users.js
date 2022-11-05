let getUsers = async () => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var users;

    await fetch(localURL + '/api/v1/usuario/', requestOptions)
        .then(response => response.text())
        .then(result => users = result)
        .catch(error => console.log('error', error));

    return JSON.parse(users);
}

let getUsersById = async (id) => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var users;

    await fetch(localURL + '/api/v1/usuario/'+id, requestOptions)
        .then(response => response.text())
        .then(result => users = result)
        .catch(error => console.log('error', error));

    return JSON.parse(users);
}


let deleteUser = async (id) => {
    var requestOptions = {
        method: 'DELETE',
        redirect: 'follow'
    };


    await fetch(localURL + '/api/v1/usuario/' + id, requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result,'Usuario deletado com sucesso'))
        .catch(error => console.log('error', error));

    window.location.reload();
}

let createUser = async ( login, password, email) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = createBody(0, login, password, email);
    
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/usuario/", requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result,'Usuario cadastrado com sucesso'))
        .catch(error => console.log('error', error));

    window.location.reload();
}

let updateUsers = async (id, login, password, email) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = createBody(id, login, password, email);

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/usuario/", requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result, 'Usuario atualizado com sucesso'))
        .catch(error => console.log('error', error));

}


function createBody(id, login, password, email){
    var raw = JSON.stringify({
        "usuario": login.toString(),
        "senha": password.toString(),
        "email": email.toString(),
        "id": parseInt(id)
    });

    return raw;
}

function callbackHandler(x, sucessMessage){
    if(x == 200){
        console.log(sucessMessage);
        window.location.reload()
        return;
    }

    alert(x);
}