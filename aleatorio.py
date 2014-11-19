import random

alunosx = open("alunosx.txt", "w")
num=1
opcao = {0: "Engenharia", 1: "Medicina", 2: "Direito", 3: "Fisica" }
while num <=300:
    nome = "Aluno" + str(num) 
    matricula = str(num)
    nota = random.randrange(100)/10.0
    dia = random.randrange(32)
    mes = random.randrange(13)
    ano = random.randrange(1980,1995)
    data = str(dia) + "/" + str(mes) + "/" + str(ano)
    op1 = random.randrange(4)
    op2 = random.randrange(4)
    while op1 == op2:
        op2 = random.randrange(4)

    linha = nome + ";" + matricula + ";" + str(nota) + ";" + data + ";" + opcao[op1] + ";" + opcao[op2]
    num += 1
    alunosx.write(linha + "\n")
