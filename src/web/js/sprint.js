let getSprints = async () => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var sprints;

    await fetch(localURL + '/api/v1/sprint/', requestOptions)
    .then(response => response.text())
    .then(result => sprints = result)
    .catch(error => console.log('error', error));

    return JSON.parse(sprints);
}

let getSprintsById = async (id) => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var sprints;

    await fetch(localURL + '/api/v1/sprint/'+ id, requestOptions)
    .then(response => response.text())
    .then(result => sprints = result)
    .catch(error => console.log('error', error));

    return JSON.parse(sprints);
}

let deleteSprint = async (id) => {
    var requestOptions = {
        method: 'DELETE',
        redirect: 'follow'
    };

    await fetch(localURL + '/api/v1/sprint/' + id, requestOptions)
    .then(response => response.text())
    .then(result => callbackHandler(result, 'Sprint deletada com sucesso'))
    .catch(error => console.log('error', error));

    window.location.reload();
}

let createSprint = async (json) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: JSON.stringify(json),
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/sprint/", requestOptions)
    .then(response => response.text())
    .then(result => callbackHandler(result, 'Cadastro efetuado com sucesso'))
    .catch(error => console.log('error', error))

    window.location.reload();
}

let updateSprint = async (json) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-type", "application/json");

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: JSON.stringify(json),
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/sprint/", requestOptions)
    .then(response => response.text())
    .then(result => callbackHandler(result, 'Atualização realizada com sucesso'))
    .catch(error => console.log('error', error));
}

function callbackHandler(response, successMessage){
    if(response == 200){
        alert(successMessage)
        window.location.reload()
        return;
    }

    alert(response);
}