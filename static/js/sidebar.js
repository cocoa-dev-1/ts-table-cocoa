const sideBar = document.querySelector('.sidebar');
let currentMenu = document.querySelectorAll('.nav-link')[0];
activate(currentMenu);

function activate(elem) {
    elem.classList.add('active');
    elem.classList.remove('link-dark');
    currentMenu = elem;
}

function deactivate(elem) {
    elem.classList.remove('active');
    elem.classList.add('link-dark');
}

function clickHandler(e) {
    let target = e.target.closest('li');
    if (!target) return
    
    if(currentMenu) {
        deactivate(currentMenu);
    }

    activate(e.target);
}

sideBar.addEventListener('click', clickHandler);