import random
def rolar_dados(inteiro):
    retorno = []
    i = 1
    while i <= inteiro:
        rolagem = random.randint(1,6)
        retorno.append(rolagem)
        i += 1
    return retorno

def guardar_dado(rolados, guardados, indice):
    retorno = []

    escolhido = rolados[indice]
    guardados.append(escolhido)
    del rolados[indice]

    retorno.append(rolados)
    retorno.append(guardados)


    return retorno

# dados_rolados =  [6, 1, 6, 4]
# dados_no_estoque = [2]
# dado_para_guardar = 2

# print(guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar))

