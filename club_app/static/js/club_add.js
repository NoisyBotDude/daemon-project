function loadMore() {
    var addInfoLink = document.getElementById('add-info-link');
    var addInfo = document.getElementsByClassName('add-info')[0];
    if (addInfo.style.display === 'none') {
        addInfo.style.display = 'block';
        addInfoLink.innerHTML = '<i class="fas fa-chevron-left"></i>' + 'Close more information';
    } else {
        addInfo.style.display = 'none';
        addInfoLink.innerHTML = '<i class="fas fa-chevron-right"></i>' + 'Add more information';
    }
}