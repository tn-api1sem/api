
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
    {
        "description": "Sprints",
        "link": "sprint.html",
        "icon": "fas fa-check-circle"
    },
]


var sidebarElement = document.getElementById("menu-navbar");
for(var i = 0; i < sidebar.length; i++ ){
    var id = sidebar[i].link;

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

var currentPage = window.location.href;
var pageHtml = currentPage.substring(currentPage.lastIndexOf('/') + 1, currentPage.length)

sidebarElement  .innerHTML = sidebarElement.innerHTML.replace(',','')
var el = document.getElementById(pageHtml)
el.classList.add('active'); 