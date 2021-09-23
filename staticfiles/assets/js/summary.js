function acc() {
    var summary = document.getElementById("summary");
    const text = summary.innerText;

    if(text=="Hide Summary")
    {
        summary.innerText = "Show Summary";
    }
    else {
        summary.innerText = "Hide Summary";
    }
}