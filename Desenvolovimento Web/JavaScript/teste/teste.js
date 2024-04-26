function faz(n){
    var s = n.toString();
    var variavel = 0;
    for (var char of s){
        var d = parseInt(char);
        variavel += d;
    }
    return variavel;
}

var resultado = faz(123123);

console.log("resultado: ", resultado)