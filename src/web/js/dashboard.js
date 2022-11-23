let getUserTeamByIdUser = async (id) => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var userTeams;

    await fetch(localURL + '/api/v1/dashboard/' + id, requestOptions)
        .then(response => response.text())
        .then(result => userTeams = result)
        .catch(error => console.log('error', error));

    return JSON.parse(userTeams);
}

let getUserRatesByIdSprint = async (id) => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var userRates;

    await fetch(localURL + '/api/v1/dashboard/userRates/' + id, requestOptions)
        .then(response => response.text())
        .then(result => userRates = result)
        .catch(error => console.log('error', error));

    return JSON.parse(userRates);
}

let getSprintByIdTeam = async () => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var teams;

    await fetch(localURL + '/api/v1/dashboard/' + id, requestOptions)
        .then(response => response.text())
        .then(result => teams = result)
        .catch(error => console.log('error', error));

    return JSON.parse(teams);

}
