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

# cursos = {0: "Engenharia", 1: "Direito", 2: "Medicina", 3: "Fisica" }

cursos = {}
faculdade = []
# alunos_cursos_1[0] = alunos da primeira opcao de engenharia
# alunos_cursos_1[1] = alunos da primeira opcao de direito ...
alunos_cursos_1 = [[],[],[],[]]

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
    Cria um dicionário com um índice e seu respectivo curso.
    """
    cursos[idx] = curso[0]
    idx += 1

print cursos
all_lines_alu = alunos.readlines() 

# Bubble Sort, algoritimo para ordernar uma lista na ordem descrecente
def bubble_sort(alunos_curso):
    """
    Bubble Sort: Algorítimo para ordernar uma lista na ordem descrescente e se a nota for igual, o mais velho prevalece.
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
    line_lst = line.strip().split(';')
    for key, curso in cursos.items():
        if line_lst[-2] == curso:
            alunos_cursos_1[key].append(line_lst) 
    
for keys in cursos.keys():
    bubble_sort(alunos_cursos_1[keys])

for alunos in alunos_cursos_1[3]:
    print alunos



# # print "####################################### ALUNOS DESCRESCENTE ######################################"
# # for aluno in alunos_eng_desc:
# #     print aluno
#
# # separar quantidade de vagas dos respectivos cursos
# for line in faculdades:
#     line_lst = line.strip().split(';')
#     if line_lst[0] == 'Engenharia':
#         vagas_engenharia = int(line_lst[1])
#
#     elif line_lst[0] == 'Medicina':
#         vagas_medicina = int(line_lst[1])
#
#     elif line_lst[0] == 'Direito':
#         vagas_direito = int(line_lst[1])
#
#     else:
#         vagas_fisica = int(line_lst[1])
#
# # lista dos aprovados nos seus respectivos cursos
# aprovados_eng = []
# aprovados_med = []
# aprovados_dir = []
# aprovados_fis = []
#
# aprovados_eng = alunos_eng_desc_1[0:vagas_engenharia]
# aprovados_med = alunos_med_desc_1[0:vagas_medicina]
# aprovados_dir = alunos_dir_desc_1[0:vagas_direito]
# aprovados_fis = alunos_fis_desc_1[0:vagas_fisica]
#
#
# # print alunos_dir_desc_1
# # print alunos_dir_desc_2
#
# # print "Alunos ENG"
# # for alunos in aprovados_eng:
# #     print alunos
# #
# # print "Alunos MED"
# # for alunos in aprovados_med:
# #     print alunos
# #
# # print "Alunos DIR"
# # for alunos in aprovados_dir:
# #     print alunos
# #
# # print "Alunos FIS:"
# # for alunos in aprovados_fis:
# #     print alunos
# # if len(aprovados_eng) < 5:
#
#
# num = 1
# while os.path.isfile("selecao%s.txt" % num):
#     num += 1
#
# else:
#     selecao = open('selecao%s.txt' % num, 'w')
#     # selecao.write('Teste')
#     
# # fechando os arquivos
# faculdades.close()
# # alunos.close()
# # selecao.close()
