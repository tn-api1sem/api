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
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

    window.location.reload();
}

let createTeam = async (nome, id_user) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "times": nome.toString(),
        "id_users": id_user,
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
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

    window.location.reload();
}

let updateUsers = async (id, id_perfil, login, password, email, celular) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "usuario": login.toString(),
        "senha": password.toString(),
        "email": email.toString(),
        "id_perfil": id_perfil,
        "celular": celular,
        "id": id
    });

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/usuario/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

}
