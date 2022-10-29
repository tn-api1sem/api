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

let createSprint = async (name, start_date, end_date, team_id, evaluation_range) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = createBody(0, name, start_date, end_date, team_id, evaluation_range)

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/sprint/", requestOptions)
    .then(response => response.text())
    .then(result => callbackHandler(result, 'Cadastro efetuado com sucesso'))
    .catch(error => console.log('error', error))

    window.location.reload();
}

let updateSprint = async (id, name, start_date, end_date, team_id, evaluation_range) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-type", "application/json");

    var raw = createBody(id, name, start_date, end_date, team_id, evaluation_range)

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/sprint/", requestOptions)
    .then(response => response.text())
    .then(result => callbackHandler(result, 'Atualização realizada com sucesso'))
    .catch(error => console.log('error', error));
}


function createBody(id, name, start_date, end_date, team_id, evaluation_range){
    return JSON.stringify({
        "name": name.toString(),
        "start_date": start_date.toString(),
        "end_date": end_date.toString(),
        "evaluation_range" : evaluation_range.toString(),
        "team_id": team_id,
        "id": id
    });
}

function callbackHandler(response, successMessage){
    if(response == 200){
        alert(successMessage)
        window.location.reload()
        return;
    }

    alert(response);
}