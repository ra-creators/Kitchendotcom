function enable() {
    var custom = document.getElementById("loft-select");

    custom.removeAttribute("disabled");

    
}

function disable() {
    var custom = document.getElementById("loft-select");

    custom.setAttribute("disabled", "");

}