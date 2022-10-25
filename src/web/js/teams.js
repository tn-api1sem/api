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

let getProfiles = async () => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var profiles;

    await fetch(localURL + '/api/v1/times', requestOptions)
        .then(response => response.text())
        .then(result => profiles = result)
        .catch(error => console.log('error', error));

    return JSON.parse(profiles);
}




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


    await fetch(localURL + '/api/v1/times/' + id, requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result, 'Time deletado com sucesso'))
        .catch(error => console.log('error', error));

    window.location.reload();
}

let createTeam = async (nome, id_user, userName) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "times": nome.toString(),
        "id_users": id_user,
        "userName": userName,
        "id": 0,
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/times/", requestOptions)
        .then(response => response.text())
        .then(result => callbackHandler(result, 'Time cadastrado com sucesso'))
        .catch(error => console.log('error', error));

}

let updateTeams = async (id, nome, id_user, userName) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "times": nome.toString(),
        "id_users": id_user,
        "userName": userName,
        "id": id,
    });

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
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