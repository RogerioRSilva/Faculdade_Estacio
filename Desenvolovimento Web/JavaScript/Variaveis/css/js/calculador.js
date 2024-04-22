var numero1 = prompt("Insira o primeiro numero: ")
var numero2 = prompt("Insira o segundo numero: ")
var operacao = prompt("Qual operação deseja realizar? ( Digite + , - , * ou / ) ")

var resultadoOperacao = realizarOperacao(numero1, numero2, operacao)

alert('O resultado da operação é = '+ resultadoOperacao)

// Outra forma de resolver esse problema com a soma
function realizarOperacao(num1, num2, op){
    var resultado = 0;

    resultado = eval(num1 + op + num2)

    return resultado
}

//var resultado = 0

// if (operacao == '+')
//     resultado = somar(numero1, numero2)

// if(operacao == '-')
//     resultado = subtrair(numero1, numero2)

// if(operacao == '*')
//     resultado = multiplicar(numero1, numero2)

// if(operacao == '/')
//     if(numero2 == 0)
//         alert("Impossivel realizar divisão por 0 !")
//     else   
//         resultado = dividir(numero1, numero2)


// alert('O resultado da operação é = '+ resultado)

// function somar(num1, num2){
//     return parseInt(num1) + parseInt(num2)
// }

// function subtrair(num1, num2){
//     return parseInt(num1) - parseInt(num2)
// }

// function multiplicar(num1, num2){
//     return parseInt(num1) * parseInt(num2)
// }

// function dividir(num1, num2){
//     return parseInt(num1) / parseInt(num2)
// }


