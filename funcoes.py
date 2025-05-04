import random
def rolar_dados(inteiro):
    retorno = []
    i = 1
    while i <= inteiro:
        rolagem = random.randint(1,6)
        retorno.append(rolagem)
        i += 1
    return retorno


