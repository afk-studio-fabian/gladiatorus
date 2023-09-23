let is_main_menu_visible = false;

function toggle_main_menu() {
    is_main_menu_visible ? hide_main_menu() : show_main_menu();
    is_main_menu_visible = !is_main_menu_visible;
}

function show_main_menu() {
    // I - 200ms - gmm-status-bar, gmm-navbar-cover
    document.getElementById("gladiatorus-main-menu-container").style.display = "grid";
    
    
    setTimeout(() => {
        document.getElementById("gladiatorus-main-menu-container").style.opacity = 1;
    document.getElementById("gladiatorus-main-menu-container").style.backgroundColor = "background-color: rgb(0 0 0 / 86%)";
        show_gmm_status_bar();
        show_gmm_navbar_cover();
    }, 100);

    // II - 400ms - gmm-core, gmm-orientation
    setTimeout(() => {
        show_gmm_core();
        show_gmm_orientation();
    }, 200);

    // Add steps III and IV as needed, using the same format.


}

function hide_main_menu() {
    // You can use the reverse order to hide the elements, or choose another sequence.
    setTimeout(() => {
        hide_gmm_orientation();
        hide_gmm_core();
    }, 100);

    setTimeout(() => {
        hide_gmm_navbar_cover();
        hide_gmm_status_bar();
        document.getElementById("gladiatorus-main-menu-container").style.opacity = 0;
        document.getElementById("gladiatorus-main-menu-container").style.backgroundColor = "background-color: rgb(0 0 0 / 0%)";
    }, 200);

    // Add more steps as needed, using the same format.

    setTimeout(() => {
        document.getElementById("gladiatorus-main-menu-container").style.display = "none";
        
    }, 600);
}

function show_gmm_status_bar() {
    let gmm_status_bar_el = document.getElementById("gmm-status-bar");
    gmm_status_bar_el.style.opacity = 1;
    gmm_status_bar_el.style.transform = "translateY(0px)"; // Assuming the element starts from translateY(500px) when hidden.
}

function hide_gmm_status_bar() {
    let gmm_status_bar_el = document.getElementById("gmm-status-bar");
    gmm_status_bar_el.style.opacity = 0;
    gmm_status_bar_el.style.transform = "translateY(-500px)";
}

// Similarly, you can add the show and hide functions for other elements:
function show_gmm_navbar_cover() {
    let el = document.getElementById("gmm-navbar-cover");
    el.style.opacity = 1;
    el.style.transform = "translateY(0px)";
    // Add other styles or transformations needed for showing.
}

function hide_gmm_navbar_cover() {
    let el = document.getElementById("gmm-navbar-cover");
    el.style.opacity = 0;
    el.style.transform = "translateY(500px)";
    // Add other styles or transformations needed for hiding.
}

function show_gmm_core() {
    let el = document.getElementById("gmm-core");
    el.style.opacity = 1;
    el.style.transform = "translateY(0px)";
    // Add other styles or transformations needed for showing.
}


function hide_gmm_core() {
    let el = document.getElementById("gmm-core");
    el.style.opacity = 0;
    el.style.transform = "translateY(-500px)";
    // Add other styles or transformations needed for hiding.
}

function show_gmm_orientation() {
    let el = document.getElementById("gmm-orientation");
    el.style.opacity = 1;
    el.style.transform = "translateY(0px)";
    // Add other styles or transformations needed for showing.
}

function hide_gmm_orientation() {
    let el = document.getElementById("gmm-orientation");
    el.style.opacity = 0;
    el.style.transform = "translateY(500px)";
    // Add other styles or transformations needed for hiding.
}
