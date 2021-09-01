function check(id) {
    const radio = document.querySelector(id)
    radio.checked = true;
  }

function checkbox_check(id) {
  const checkbox = document.querySelector(id)
  if(checkbox.checked === true) {
    checkbox.checked = false;
  }
  else {
    checkbox.checked = true;
  }
}