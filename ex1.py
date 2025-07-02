'''
Administrativo
Operacional
Tecnico
funcao que receba essas 3 listas e retorne um unico dicionario onde as chaves seja os nomes dos departamentos, os valores SAO TUPLAS, contendo os nomes dos funcionarios
mas apenas se tiver mais que 2 participantes, 
'''


def dic_setores(**setor):
    Administrativo = setor.get('adm')
    Operacional = setor.get('opc')
    Tecnico = setor.get('tcn')


    dicionario = {'Administrativo': tuple(Administrativo), 'Operacional': tuple(Operacional), 'Tecnico': tuple(Tecnico)}
    return dicionario
    

def ordem(lista):
    valor = [x for sub in lista.values() for x in sub]

    valor.sort()

    return valor


adms = ['Vinicius', 'Wesley', 'Seila']    
opcs = ['Vinicius', 'Wesley']    
tcns = ['Vinicius', 'Wesley']   

print(dic_setores(adm = adms, opc = opcs, tcn = tcns))

# print(ordem(dic_setores(adm = adms, opc = opcs, tcn = tcns)))









