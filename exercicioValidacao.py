
#Exercício 1 

class Validacao:
    idade = None
    def __init__(self):
        pass

    def InserirNome(self, nome):
        nomeCorreto = self.ValidaNome(nome)
        if nomeCorreto == True:
            self.nome = nome
            print("")

    def ValidaNome(self, nome):
        if (len(nome) > 0):
            return True
        else:
            print("O Nome precisa ter mais que 1 caractere")
            return False


    idade = None
    def __init__(self):
        pass

    def InserirIdade(self, idade):
        idadeCorreta = self.ValidaIdade(idade)
        if idadeCorreta == True:
            self.idade = idade
            print("")

    def ValidaIdade(self, idade):
        if idade <= 18:
            print("Idade precisa ser maior de 18")
            return False
        else:
            return True
        
    saldo = None
    def __init__(self):
        pass

    def InserirSaldo(self, saldo):
        saldoCorreto = self.ValidaSaldo(saldo)
        if saldoCorreto == True:
            self.saldo = saldo
            print("")

    def ValidaSaldo(self, saldo):
        if saldo <= 0:
            print("O saldo precisa ser positivo")
            return False
        else:
            return True

    
    statusCadastro = None
    def __init__(self):
        pass

    def statusCadastro(self, statusCadastro):
        statusCorreto = self.ValidaStatus(statusCadastro)
        if statusCorreto == True:
            self.statusCadastro = statusCadastro
            print("Dados cadastrados com sucesso")

    def ValidaStatus(self, statusCadastro):
        if statusCadastro == "Verdadeiro":
            return True
        else:
            print("O cadastro deve ser verdadeiro")
            return False

cadastro1 = Validacao()
cadastro1.InserirNome("Julio")
cadastro1.InserirIdade(20)
cadastro1.InserirSaldo(1294)
cadastro1.statusCadastro("Verdadeiro")