from functools import reduce


aluno = ('Vinicius', 5), ('Leonardo', 2), ('Beto', 1), ('Matheus', 7)


def academia(num):

    pessoas = [x for x in num]

    filtro = list(filter(lambda x: x[1] >= 3, pessoas))

    ativos = [x for x in filtro]


    return ativos
 



print(academia(aluno))


