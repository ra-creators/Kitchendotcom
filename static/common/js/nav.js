function navButton() {
  var x = document.getElementById("nav-links");
  if (x.className === "links") {
    x.className += " responsive";
  } else {
    x.className = "links";
  }
}
