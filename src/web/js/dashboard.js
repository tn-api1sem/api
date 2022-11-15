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