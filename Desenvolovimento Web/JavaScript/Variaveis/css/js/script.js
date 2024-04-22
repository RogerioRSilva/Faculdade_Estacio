// Tipos nativos
var a = 10.5;

let b = "XPTO";

const c = true;

a += 2;

if(a <= 20){
    a *= 5;
}

console.log(a)

// Funções normais
function somar(num1, num2){
    return num1 + num2;
}
console.log("Resultado da função soma: ", somar(20, 30))

// Função Arrow Function
let somarAF = (num1, num2) => num1 + num2;

console.log("Resultado Arrow Function: ", somarAF(40, 20))


// Utilizando Vetores:
// Utilizando o Array
let v1 = new Array(15, 21, 32);

console.log(v1)

// Criando um vetor direto utilizando []
let v2 = [10, 20, 30];

console.log(v2)
