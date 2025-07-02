from random import randint

def faturamento():
    faturar = [randint(100, 500) for x in range(1000)]

    return faturar

def preco(*valores, **descontos):
    desconto_p = descontos.get('desc_percentual')
    desconto_f = descontos.get('desc_fixo')


    for valor in valores:
        if desconto_p and desconto_f:
            (valor - desconto_p) - desconto_f
        else:
            (valor - desconto_f)
        return valor


percentual = 7/100
fixo = 50

print(preco(faturamento()), desc_percentual = percentual, desc_fixo = fixo)
        