let getTeams = async () => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var teams;

    await fetch(localURL + '/api/v1/times/', requestOptions)
        .then(response => response.text())
        .then(result => teams = result)
        .catch(error => console.log('error', error));

    return JSON.parse(teams);
}

let getTeamById = async (id) => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var teams;

    await fetch(localURL + '/api/v1/times/' + id, requestOptions)
        .then(response => response.text())
        .then(result => teams = result)
        .catch(error => console.log('error', error));

    return JSON.parse(teams);
}


let deleteTeam = async (id) => {
    var requestOptions = {
        method: 'DELETE',
        redirect: 'follow'
    };

    console.log(id);

    await fetch(localURL + '/api/v1/times/' + id, requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result, 'Time deletado com sucesso'))
        .catch(error => console.log('error', error));

    window.location.reload();
}

let createTeam = async (raw) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: JSON.stringify(raw),
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/times/", requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result, 'Time cadastrado com sucesso'))
        .catch(error => console.log('error', error));

}

let updateTeams = async (raw) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: JSON.stringify(raw),
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/times/", requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result, 'Time atualizado com sucesso'))
        .catch(error => console.log('error', error));

}

function callbackHandler(x, successMessage) {
    if (x == 200) {
        console.log(successMessage)
        window.location.reload()
        return;
    }

    alert(x);
}