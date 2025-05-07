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

def remover_dado(rolados, guardados, removido):
    retorno = []

    rolados.append(guardados[removido])
    del guardados[removido]

    retorno.append(rolados)
    retorno.append(guardados)

    return retorno

# dados_rolados = [2, 2, 2, 2]
# dados_no_estoque = [1]
# dado_para_remover = 0

# print(remover_dado(dados_rolados, dados_no_estoque, dado_para_remover))

def calcula_pontos_regra_simples(rolados):
    retorno = {face: rolados.count(face) * face for face in range(1,7)}
    return retorno
# print(calcula_pontos_regra_simples([2, 3, 4, 5, 2]))

def calcula_pontos_soma(rolados):
    i = 0
    soma = 0
    nrolados = len(rolados)    

    while i < nrolados:
        soma += rolados[i]
        i += 1
    return soma
# print(calcula_pontos_soma([2, 3, 4, 5, 2]))

def calcula_pontos_sequencia_baixa(rolados):
    i = 0
    while i < len(rolados):
        atual = rolados[i]
        tem1 = False
        tem2 = False
        tem3 = False

        j = 0
        while j < len(rolados):
            if rolados[j] == atual + 1:
                tem1 = True
            if rolados[j] == atual + 2:
                tem2 = True
            if rolados[j] == atual + 3:
                tem3 = True
            j += 1

        if tem1 and tem2 and tem3:
            return 15

        i += 1

    return 0
# print(calcula_pontos_sequencia_baixa([2, 3, 4, 6, 2]))

def calcula_pontos_sequencia_alta(dado):
    unico = list(set(dado))
    pontos = 0

    pontuacao =  [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6]
    ]

    for sequencia in pontuacao:
        existe = True

        for numero in sequencia:
            if numero not in unico:
                existe = False
                break
        if existe:
            pontos = 30
            return pontos
    return pontos

# print(calcula_pontos_sequencia_alta([5, 4, 1, 3, 2, 1]))

def calcula_pontos_full_house(lista):
    pontuacao = 0
    quantidade = len(lista)
    tira_repetido = list(set(lista))

    if len(tira_repetido) < 2:
        return pontuacao
    
    dicio = {}
    i = 0

    while i < quantidade:
        if lista[i] not in dicio:
            dicio[lista[i]] = 1
        else:
            dicio[lista[i]] += 1

        pontuacao += lista[i]
        i += 1

    if 3 in dicio.values() and 2 in dicio.values():
        return pontuacao
    
    return 0 

# print(calcula_pontos_full_house([5, 2, 5, 5, 2]))

def calcula_pontos_quadra(lista):
    pontuacao = 0
    quantidade = len(lista)

    dicio = {}
    i = 0

    while i < quantidade:
        if lista[i] not in dicio:
            dicio[lista[i]] = 1
        else:
            dicio[lista[i]] += 1

        pontuacao += lista[i]
        i += 1

    for repeticao in dicio.values():
        if repeticao >= 4:
            return pontuacao
    
    return 0

# print(calcula_pontos_quadra([5, 2, 5, 5, 5, 1]))

def calcula_pontos_quina(lista):
    unico = []
    contagem = []

    for i in range(len(lista)):
        valor = lista[i]
        achado = False

        for k in range(len(unico)):
            if unico[k] == valor:
                contagem[k] += 1
                achado = True
                break

        if not achado:
            unico.append(valor)
            contagem.append(1)

    for i in range(len(contagem)):
        if contagem[i] >= 5:
            return 50
    
    return 0

# print(calcula_pontos_quina([5, 2, 5, 5, 5, 5]))