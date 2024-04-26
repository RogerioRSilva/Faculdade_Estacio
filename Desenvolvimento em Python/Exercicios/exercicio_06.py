# Validar notas do aluno

nota_aluno = float(input("Qual a sua nota? "))

if(nota_aluno >= 7):
    print(f'Você foi aprovado com nota {nota_aluno}')
elif(nota_aluno >= 5 and nota_aluno < 7):
    print(f'Você está em recuperação com nota {nota_aluno}')
else:
    print(f'Você está reprovado com nota {nota_aluno}')