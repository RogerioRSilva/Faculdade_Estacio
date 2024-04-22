// Entrada de dados, é exibido uma janela com campo para inserir os dados. 
var numero1 = prompt("Insira o primeiro número: ");
var numero2 = prompt("Insira o segundo número: ");

// Executa a função dividir e insere o resultado dentro da variavel
var resultadoDivisao = divida(numero1, numero2); 

// Retorna o resultado para o usuário em uma caixa de dialogo (Janela)
alert('O resultado da divisão é igual a: '+ resultadoDivisao); 

// Função de divizão dos dados
function divida(numero1, numero2){

    var resultado = 0; 

    resultado = numero1 / numero2;

    return resultado;

}


