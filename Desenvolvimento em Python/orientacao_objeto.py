# Criando uma classe
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.set_nome(nome)
        self.set_sobrenome(sobrenome)

    def set_nome(self, nome):
        self.nome=nome

    def set_sobrenome(self, sobrenome):
        self.sobrenome=sobrenome

    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome

# Criando os objetos
pessoa1 = Pessoa("Rogério", "Silva")
pessoa2 = Pessoa("Michele", "Cintra")

print(f'{pessoa1.get_nome()} {pessoa1.get_sobrenome()}')
print(f'{pessoa2.get_nome()} {pessoa2.get_sobrenome()}')