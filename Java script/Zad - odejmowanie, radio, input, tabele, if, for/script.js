let button = document.getElementById('button');
let wynik = document.getElementById('wynik');

button.onclick = function() {
    let radjo = document.getElementsByName('radio');
    let monka = document.getElementById('monka').value;
    for (walju of radjo) {
        if(walju.checked) {
            if(parseInt(walju.value) <= monka) {
                const lista = ["a", "b", "c", "d", "e", `potrzebujesz ${walju.value}g monki`]
                document.getElementById("table").innerHTML = ""
                for (i of lista) {
                    document.getElementById("table").innerHTML += "<tr><td>" + i + "</td></tr>";
                }
            }
        }
    }
}