function loadMore() {
    var addInfoLink = $('#add-info-link');
    var addInfo = $('.add-info')[0];
    if (addInfo.style.display === 'none') {
        addInfo.style.display = 'block';
        addInfoLink.innerHTML = '<i class="fas fa-chevron-left"></i>' + 'Close more information';
    } else {
        addInfo.style.display = 'none';
        addInfoLink.innerHTML = '<i class="fas fa-chevron-right"></i>' + 'Add more information';
    }
}


// for name of core memmbers
var table1 = document.querySelector("#core-members");
var index1 = table1.rows.length;

function addRow1(index) {
    var newRow = table1.insertRow(index);
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    cell1.innerHTML = "<td><input type='text' name='core-members-name-" + (index-1) + "' id='core-members-name' placeholder='Name' required></td>"
    cell2.innerHTML = "<td><input type='text' name='core-members-designation-" + (index-1) + "' id='core-members-designation' placeholder='Designation' required></td>"
}

$(".add-details").eq(0).on("click", function() {
    addRow1(index1);
    index1++;
});

// for contact of core memmbers
var table2 = document.querySelector("#contact-details");
var index2 = table2.rows.length;

function addRow2(index) {
    var newRow = table2.insertRow(index);
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    cell1.innerHTML = "<td><input type='text' name='contact-details-name-" + (index-1) + "' id='contact-details-name' placeholder='Name' required></td>"
    cell2.innerHTML = "<td><input type='text' name='contact-details-number-" + (index-1) + "' id='contact-details-number' placeholder='Contact' required></td>"
}

$(".add-details").eq(1).on("click", function() {
    addRow2(index2);
    index2++;
});