function randint(n1, n2) {
    return Math.floor(Math.random() * (n2 - n1)) + n1;
}

function carregarpostos() {
    document.getElementById("posto1").innerHTML = "Posto Mapunda<br>"+randint(1, 50)+"kg";
    document.getElementById("posto2").innerHTML = "Posto Lucrecia<br>"+randint(1, 50)+"kg";
    document.getElementById("posto3").innerHTML = "Posto Tchioco<br>"+randint(1, 50)+"kg";
    document.getElementById("posto4").innerHTML = "Posto Minhota<br>"+randint(1, 50)+"kg";
    document.getElementById("posto5").innerHTML = "Posto Arco Iris<br>"+randint(1, 50)+"kg";
    document.getElementById("posto6").innerHTML = "Posto Lage<br>"+randint(1, 50)+"kg";
    document.getElementById("posto7").innerHTML = "Posto Laureanos<br>"+randint(1, 50)+"kg";
    document.getElementById("posto8").innerHTML = "Posto Bairro Comercial<br>"+randint(1, 50)+"kg";
}

function esvaziarpostos() {
    document.getElementById("posto1").innerHTML = "Posto Mapunda<br>0kg";
    document.getElementById("posto2").innerHTML = "Posto Lucrecia<br>0kg";
    document.getElementById("posto3").innerHTML = "Posto Tchioco<br>0kg";
    document.getElementById("posto4").innerHTML = "Posto Minhota<br>0kg";
    document.getElementById("posto5").innerHTML = "Posto Arco Iris<br>0kg";
    document.getElementById("posto6").innerHTML = "Posto Lage<br>0kg";
    document.getElementById("posto7").innerHTML = "Posto Laureanos<br>0kg";
    document.getElementById("posto8").innerHTML = "Posto Bairro Comercial<br>0kg";
}