"""
Trabalho de MCG126 - Programacao Computacional II
Renan Ermida Fontes. DRE: 
"""
# NOME e DRE

import os.path

# open faculdade.txt
faculdade = open('faculdade.txt', 'r')

# open alunos.txt
alunos = open ('alunos.txt', 'r')

# cursos = ['Engenharia', 'Medicina', 'Direito', 'Fisica']
# inicializar alunos dos respectivos curso
alunos_eng_desc = []
alunos_engenharia_1 = []
alunos_engenharia_2 = []

alunos_med_desc = []
alunos_medicina_1 = []
alunos_medicina_2 = []

alunos_dir_desc = []
alunos_direito_1 = []
alunos_direito_2 = []

alunos_fis_desc = []
alunos_fisica_1 = []
alunos_fisica_2 = []

alunos_total = []

# Bubble Sort, algoritimo para ordernar uma lista na ordem descrecente
def bubble_sort(alunos_curso):
    cp_alunos_curso = list(alunos_curso)
    for i in range(len(cp_alunos_curso)-1):
        for j in range(len(cp_alunos_curso)-1-i):
            if cp_alunos_curso[j][2] < cp_alunos_curso[j+1][2]:
                cp_alunos_curso[j], cp_alunos_curso[j+1] = cp_alunos_curso[j+1], cp_alunos_curso[j]
           
           # se tiverem a mesma nota, e o anterior for mais novo, troca pois a preferencia e dos mais velhos
            elif cp_alunos_curso[j][2] == cp_alunos_curso[j+1][2]:
                if int(cp_alunos_curso[j][3][-4:]) > int(cp_alunos_curso[j+1][3][-4:]):
                    cp_alunos_curso[j], cp_alunos_curso[j+1] = cp_alunos_curso[j+1], cp_alunos_curso[j]

    return cp_alunos_curso

# separar alunos dos respectivos cursos
for line in alunos:
    line_lst = line.strip().split(';')
    alunos_total.append(line_lst)
    if line_lst[-2] == "Engenharia":
        alunos_engenharia_1.append(line_lst)

    elif line_lst[-1] == "Engenharia":
        alunos_engenharia_2.append(line_lst)

    elif line_lst[-2] == "Medicina" :
        alunos_medicina_1.append(line_lst)

    elif line_lst[-1] == "Medicina":
        alunos_medicina_2.append(line_lst)
        
    elif line_lst[-2] == "Direito" 
        alunos_direito_1.append(line_lst)

    elif line_lst[-1] == "Direito":
        alunos_direito_2.append(line_lst) 

    elif line_lst[-2] == "Fisica": 
        alunos_fisica_1.append(line_lst)

    elif line_lst[-1] == "Fisica":
        alunos_fisica_2.append(line_lst)

    # else:
    #     alunos_fisica.append(line_lst)


# Ordernar alunos dos repsectivos cursos na ordem descrecente
alunos_eng_desc_1 = bubble_sort(alunos_engenharia_1)
alunos_eng_desc_2 = bubble_sort(alunos_engenharia_2)
alunos_eng_desc.extend(alunos_eng_desc_1)
alunos_eng_desc.extend(alunos_eng_desc_2)

alunos_med_desc = bubble_sort(alunos_medicina)
alunos_dir_desc = bubble_sort(alunos_direito)
alunos_fis_desc = bubble_sort(alunos_fisica)
alunos_total_desc = bubble_sort(alunos_total)

print "####################################### ALUNOS DESCRESCENTE ######################################"
for aluno in alunos_eng_desc:
    print aluno

# separar quantidade de vagas dos respectivos cursos
# for line in faculdade:
#     line_lst = line.split(';')
#     print line_lst[0]
#     if line_lst[0] == 'Engenharia':
#         vagas_engenharia = line_lst[1]
#
#     elif line_lst[0] == 'Medicina':
#         vagas_medicina = line_lst[1]
#
#     elif line_lst[0] == 'Direito':
#         vagas_direito = line_lst[1]
#
#     else:
#         vagas_fisica = line_lst[1]

num = 1
while os.path.isfile("selecao%s.txt" % num):
    num += 1

else:
    selecao = open('selecao%s.txt' % num, 'w')
    # selecao.write('Teste')
    
# fechando os arquivos
faculdade.close()
alunos.close()
# selecao.close()
