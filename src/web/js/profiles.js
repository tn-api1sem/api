let getProfiles = async () => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var profiles;

    await fetch(localURL + '/api/v1/profile', requestOptions)
        .then(response => response.text())
        .then(result => profiles = result)
        .catch(error => console.log('error', error));

    return JSON.parse(profiles);
}
