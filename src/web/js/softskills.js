let getSoftSkills = async () => {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    var skills;

    await fetch(localURL + '/api/v1/softskills', requestOptions)
        .then(response => response.text())
        .then(result => skills = result)
        .catch(error => console.log('error', error));

    return JSON.parse(skills);
}
