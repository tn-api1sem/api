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

let deleteUser = async (id) => {
    var requestOptions = {
        method: 'DELETE',
        redirect: 'follow'
    };


    await fetch(localURL + '/api/v1/usuario/' + id, requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

    return JSON.parse(users);
}