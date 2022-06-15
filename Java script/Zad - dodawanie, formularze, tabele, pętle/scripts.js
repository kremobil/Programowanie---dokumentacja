let table = document.getElementById('table');
let button = document.getElementsByTagName('button')[0];

button.addEventListener('click', generation)

function generation(){
    let maxA = document.getElementById('maxA').value;
    let maxB = document.getElementById('maxB').value;
    let numberA
    let numberB
    let resultA = 0;
    let resultB = 0;
    table.innerHTML = "<tr><td>Liczba A</td><td>Liczba B</td></tr>";
    for (let i = 0; i < 10; i++) {
        numberA = Math.round(maxA * Math.random());
        numberB = Math.round(maxB * Math.random());
        table.innerHTML += "<tr><td>"+numberA+"</td><td>"+numberB+"</td></tr>";
        resultA += numberA;
        resultB += numberB;
        console.log(numberB)
    }
    table.innerHTML += "<tr><td>"+resultA+"</td><td>"+resultB+"</td></tr>";
}