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

// function addRow() {
//     let x = 2;

//     let row = document.createElement('tr');
//     let column1 = document.createElement("td");

//     const column1text = document.createTextNode(`Row ${x} Column 1`);

//     column1.appendChild(column1text);
//     let column2 = document.createElement("td");
//     const column2text = document.createTextNode(`Row ${x} Column 2`);
//     column2.appendChild(column2text);

//     row.appendChild(column1);
//     row.appendChild(column2);

//     document.getElementsByClassName('table').appendChild(row);
//     x++;
// }

function addRowMembers() {
    var table = document.getElementById("table-1");
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = "<input type='text' name= 'core-members' id='core-members-name-1' placeholder='Name' required>"
    cell2.innerHTML = "<input type='text' name= 'core-members' id='core-members-details-1' placeholder='Designation' required>";
}

function addRowContacts() {
    var table = document.getElementById("table-2");
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = "<input type='text' name= 'core-members' id='core-members-name-2' placeholder='Name' required>"
    cell2.innerHTML = "<input type='text' name= 'core-members' id='core-members-details-2' placeholder='Contact' required>";
}