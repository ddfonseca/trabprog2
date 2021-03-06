"""
Trabalho de MCG126 - Programacao Computacional II
Renan Ermida Fontes. DRE: 
"""
# Renan Ermida Fontes e DRE

import os.path

# open faculdade.txt
faculdades = open('faculdades.txt', 'r')

# open alunos.txt
alunos = open ('alunos.txt', 'r')


cursos = {}
faculdade = []
# alunos_cursos_1[0] = alunos da primeira opcao de engenharia
# alunos_cursos_1[1] = alunos da primeira opcao de medicina...
alunos_cursos_1 = []
alunos_cursos_2 = []
aprovados_cursos = []
nao_aprovados_cursos = []
reclassificados_cursos = []

all_lines_fac = faculdades.readlines()
for line in all_lines_fac:
    """
    Separa o nome da faculdade e a vaga respectivamente na lista faculdade.
    """
    facul_vaga = line.strip().split(';')
    faculdade.append(facul_vaga)

idx = 0
for curso in faculdade:
    """
    Cria um dicionario com um indice e seu respectivo curso.
    """
    cursos[idx] = curso[0]
    idx += 1

for num_cursos in range(idx):
    """
    Iniciando as variaveis de acordo com o numero de cursos.
    """
    alunos_cursos_1.append([])
    alunos_cursos_2.append([])
    aprovados_cursos.append([])
    nao_aprovados_cursos.append([])
    reclassificados_cursos.append([])

all_lines_alu = alunos.readlines() 

# Bubble Sort, algoritimo para ordernar uma lista na ordem descrecente
def bubble_sort(alunos_curso):
    """
    Bubble Sort: Algoritimo para ordernar uma lista na ordem descrescente e se a nota for igual, o mais velho prevalece.
    """
    for i in range(len(alunos_curso)-1):
        for j in range(len(alunos_curso)-1-i):
            if alunos_curso[j][2] < alunos_curso[j+1][2]:
                alunos_curso[j], alunos_curso[j+1] = alunos_curso[j+1], alunos_curso[j]
           
           # se tiverem a mesma nota, e o anterior for mais novo, troca pois a preferencia e dos mais velhos
            elif alunos_curso[j][2] == alunos_curso[j+1][2]:
                if int(alunos_curso[j][3][-4:]) > int(alunos_curso[j+1][3][-4:]):
                    alunos_curso[j], alunos_curso[j+1] = alunos_curso[j+1], alunos_curso[j]

# separar cada aluno da primeira opcao em cada curso em alunos_cursos_1
for line in all_lines_alu:
    """
    Separa cada aluno de cada curso de acordo com sua primeira opcao e segunda opcao
    """
    line_lst = line.strip().split(';')
    for key, curso in cursos.items():
        # se escolheu o curso da primeira opcao, adicione ao alunos_cursos_1
        if line_lst[-2] == curso:
            alunos_cursos_1[key].append(line_lst)
        
        #se escolheu o curso da segunda opcao, adicione ao alunos_cursos_2
        elif line_lst[-1] == curso:
            alunos_cursos_2[key].append(line_lst)

for key in cursos.keys():
    """
    Ordernar de ordem descrescente de notas as listas.
    """
    bubble_sort(alunos_cursos_1[key])
    bubble_sort(alunos_cursos_2[key])

# lista dos aprovados nos seus respectivos cursos

for key, curso in cursos.items():
    """
    Separa os aprovados de cada curso e os nao aprovados, assim como ordena na ordem descrescente os nao aprovados.
    """
    vagas = int(faculdade[key][1])
    selecionados_1 = alunos_cursos_1[key][0:vagas]
    nao_aprovados = alunos_cursos_1[key][vagas:]
    aprovados_cursos[key].extend(selecionados_1)
    nao_aprovados_cursos[key].extend(nao_aprovados)
    bubble_sort(nao_aprovados_cursos[key])

for key, curso in cursos.items():
    """
    Todos que nao foram aprovados nos seus respectivos cursos, serao alocados em uma nova lista de reclassificados de acordo com sua segunda opcao de curso assim como ordernar essa nova lista na ordem descrescente
    """
    vagas = int(faculdade[key][1])
    # if len(aprovados_cursos[key]) < vagas:
    for key_2 in cursos.keys():
        for aluno in nao_aprovados_cursos[key_2]:
            if aluno[-1] == curso:
                reclassificados_cursos[key].append(aluno)

    bubble_sort(reclassificados_cursos[key])

for key in cursos.keys():
    """
    Se houver vaga sobrando em algum curso, alocar os que estao na reclassificacao para tais cursos de acordo com sua nota. Quem escolheu a primeira opcao tem preferencia mesmo com nota menor.
    """
    vagas = int(faculdade[key][1])
    while len(aprovados_cursos[key]) < vagas:
        # reclassificados_cursos viram nao_aprovados
        aluno_reclassificado = reclassificados_cursos[key].pop(0)
        aprovados_cursos[key].append(aluno_reclassificado)

# Enquanto for verdade que existe o arquivo selecao%NUM.txt entao adicione 1 ao num e entao crie tal arquivo
num = 1
while os.path.isfile("selecao%s.txt" % num):
    num += 1
else:
    selecao = open('selecao%s.txt' % num, 'w')


selecao.write('Curso; # de vagas; # de selecionados; matriculas\n')
for key in cursos.keys():
    linha = "%s\t%i\t%i" % (faculdade[key][0], int(faculdade[key][1]), len(aprovados_cursos[key]))
    for aluno in aprovados_cursos[key]:
        matricula = aluno[1]
        linha += "\t" + str(matricula)
    selecao.write(linha + '\n')



# fechando os arquivos
faculdades.close()
alunos.close()
selecao.close()
