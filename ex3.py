from random import randint
from functools import reduce

def faturamento():
    faturar = [randint(100, 500) for x in range(10)]
    return faturar
 

def preco(*valores, **descontos):
    desconto_p = descontos.get('desc_percentual')
    desconto_f = descontos.get('desc_fixo')


    for a in valores:
        if not desconto_p:
            valor = [(x-desconto_f) for x in valores]
        else:
            valor = [((x*desconto_p)-desconto_f) for x in valores]

    return valor
    


print(preco(faturamento(), desc_percentual = 0.93, desc_fixo = 50))
# print(faturamento())
        