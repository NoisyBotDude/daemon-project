function loadMore() {
    var more = document.getElementById("more");
    var more_btn = document.getElementById("more-btn");
    
    if (more.style.display == "block") {
        more.style.display = "none";
        more_btn.innerHTML = "More";
        // h1.style.annimatinPlayState = "running";
    } else {
        more.style.display = "block";
        more_btn.innerHTML = "Less";
        more.style.animationPlayState = "running";
    }
}