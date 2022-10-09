//Sidebar 
// 1 - Admin
// 2 - Usuario
var sidebar = [
    {
        "description": "Dashboard",
        "link": "index.html",
        "icon": "fas fa-tachometer-alt",
        "allowed-users": [1,2]
    },
    {
        "description": "Usuarios",
        "link": "users.html",
        "icon": "fas fa-user",
        "allowed-users": [1]
    },
    {
        "description": "Sprints",
        "link": "sprint.html",
        "icon": "fas fa-check-circle",
        "allowed-users": [1]
    },
    {
        "description": "Times",
        "link": "teams.html",
        "icon": "fas fa-users"
    },
]

var user = JSON.parse(window.localStorage.getItem('user'));
console.log(user)
var sidebarElement = document.getElementById("menu-navbar");
for (var i = 0; i < sidebar.length; i++) {
    var id = sidebar[i].link;

    if(sidebar[i]["allowed-users"].includes(user.id_perfil))
        sidebarElement.innerHTML += 
        `
            <li id="${id}">
                <a 
                    href="${sidebar[i].link}"  
                >
                    <i class="${sidebar[i].icon}"></i>${sidebar[i].description}
                </a>
            </li>
        `
}

//Sidebar active
var currentPage = window.location.href;
var pageHtml = currentPage.substring(currentPage.lastIndexOf('/') + 1, currentPage.length)

sidebarElement.innerHTML = sidebarElement.innerHTML.replace(',', '')
var el = document.getElementById(pageHtml)
el.classList.add('active'); 


