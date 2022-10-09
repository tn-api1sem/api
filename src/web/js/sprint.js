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
    .then(result => console.log(result))
    .catch(error => console.log('error', error));

    window.location.reload();
}

let createSprint = async (name, start_date, end_date, team_id) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "nome": name.toString(),
        "datainicio": start_date.toString(),
        "dataentrega": end_date.toString(),
        "time": team_id,
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/sprint/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error))

    window.location.reload();
}

let updateSprint = async (id, name, start_date, end_date, team_id) => {
    var myHeaders = new Headers();
    myHeaders.append("Content-type", "application/json");

    var raw = JSON.stringify({
        "nome": name.toString(),
        "datainicio": start_date.toString(),
        "dataentrega": end_date.toString(),
        "time": team_id,
        "id": id
    });

    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    await fetch(localURL + "/api/v1/sprint/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
}