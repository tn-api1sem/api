
var sidebar = [
    {
        "description": "Dashboard",
        "link": "index.html",
        "icon": "fas fa-tachometer-alt"
    },
    {
        "description": "Usuarios",
        "link": "users.html",
        "icon": "fas fa-user"
    },
]


var sidebarElement = document.getElementById("menu-navbar");
for(var i = 0; i < sidebar.length; i++ ){
    sidebarElement.innerHTML += 
    `
        <li>
        <a href="${sidebar[i].link}">
            <i class="${sidebar[i].icon}"></i>${sidebar[i].description}</a>
        </li>
    `
}