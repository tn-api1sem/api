let getUserRates = async () => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var teams;

    await fetch(localURL + '/api/v1/avaliacaoUsuario/', requestOptions)
        .then(response => response.text())
        .then(result => teams = result)
        .catch(error => console.log('error', error));

    return JSON.parse(teams);
}