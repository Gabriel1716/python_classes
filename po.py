class Exercicios:
    def __init__(self):
        print("-")

    def exercicio1(self,nome,idade,salario,cargo,turno,setor):
        print("Meu nome é", nome, "tenho", idade, "anos," "ganho," "R$", salario, "meu cargo é", cargo, "trabalho no período", turno, "no setor", setor)
    
    def exercicio2(self,nomeEscola,estado,numeroProfessores,cidade,numeroMilitares,logradouro,numeroEndereco,numeroAlunos,colegioMilitar,disciplinas):
        print("O nome da minha escola é:", nomeEscola, "pertence ao estado:", estado, "tem", numeroProfessores, "professores", "pertence a cidade:", cidade, "tem",
             numeroMilitares, "de militares e fica em", logradouro, "seu número é:", numeroEndereco, "tem", numeroAlunos, "alunos", "é um", colegioMilitar,
             "e possui", disciplinas )

ex = Exercicios()
ex.exercicio1(nome = "Gustavo", idade = 14, salario = "1.980", cargo = "auxiliar", turno = "manhã", setor = "RH")
ex.exercicio2(nomeEscola = "Estadual", estado = "Paraná", numeroProfessores = 30, cidade = "Cruzeiro do Oeste", numeroMilitares = 4, logradouro = "Rua Tchurusbango",
              numeroEndereco = 4124, numeroAlunos = 620, colegioMilitar = True, disciplinas = "português, matemática, física")