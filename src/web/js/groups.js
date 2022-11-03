let groupUrl = localURL + '/api/v1/usuario/';

let getGroups = async () => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var groups = [];

    await fetch(groupUrl, requestOptions)
        .then(response => response.text())
        .then(result => groups = result)
        .catch(error => console.log('error', error));

    return JSON.parse(users);
}

let getGroupById = async (id) => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var group;

    await fetch(groupUrl+id, requestOptions)
        .then(response => response.text())
        .then(result => group = result)
        .catch(error => console.log('error', error));

    return JSON.parse(group);
}

let createGroup = async (jsonData) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: jsonData,
        redirect: 'follow'
    };

    await fetch(groupUrl, requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result, 'Grupo cadastrado com sucesso'))
        .catch(error => console.log('error', error));

    window.location.reload();
}

let updateGroup = async (jsonData) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: jsonData,
        redirect: 'follow'
    };

    await fetch(groupUrl, requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result, 'Grupo atualizado com sucesso'))
        .catch(error => console.log('error', error));

}

let deleteGroup = async (id) => {
    var requestOptions = {
        method: 'DELETE',
        redirect: 'follow'
    };

    await fetch(groupUrl + id, requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result,'Grupo deletado com sucesso'))
        .catch(error => console.log('error', error));

    window.location.reload();
}

function callbackHandler(x, sucessMessage){
    if(x == 200){
        console.log(sucessMessage);
        window.location.reload()
        return;
    }

    alert(x);
}