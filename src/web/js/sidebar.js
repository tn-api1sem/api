//Sidebar 
// 1 - Admin
// 2 - Usuario
var sidebar = [
    {
        "description": "Dashboard",
        "link": "index.html",
        "icon": "fas fa-tachometer-alt",
        "admin-only": false
    },
    {
        "description": "Usuários",
        "link": "users.html",
        "icon": "fas fa-user",
        "admin-only": true
    },
    {
        "description": "Times",
        "link": "teams.html",
        "icon": "fas fa-users",
        "admin-only": true
    },
    {
        "description": "Turmas",
        "link": "groups.html",
        "icon": "fas fa-globe",
        "admin-only": true
    },
    {
        "description": "Sprints",
        "link": "sprint.html",
        "icon": "fas fa-check-circle",
        "admin-only": true
    }
]

var user = JSON.parse(window.localStorage.getItem('user'));
console.log(user)
var sidebarElement = document.getElementById("menu-navbar");
for (var i = 0; i < sidebar.length; i++) {
    var id = sidebar[i].link;
    
    if(sidebar[i]["admin-only"] && user.usuario != 'admin')
        continue;
    
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


