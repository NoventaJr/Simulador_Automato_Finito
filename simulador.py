import pprint

#af é o dicionário que será utilizado para percorrer os estados do automato
af = {}

#Quantidade de estados
n_estados = int(input())
if (n_estados > 10 or n_estados < 1):
    print('O número de estados deve ser no mínimo 1 e no máximo 10')
    exit()
    
#Inicializando o dicionário (transições) para cada estado
for x in range(n_estados):
    af[str(x)] = {}

#Quantidade de símbolos terminais + símbolos terminais (uma linha)
terminais = input()
simb_terminais = terminais.split()
n_simb_terminais = int(simb_terminais[0])
if (n_simb_terminais > 10):
    print('O número máximo de símbolos terminais é 10')
    exit()
simb_terminais.pop(0)

#Quantidade de estados iniciais
#AFD = 1, estado_inicial = q0
#AFN = n (n >= 1), estado_inicial = [q0, q1, ..., qn]
n_iniciais = int(input())
if (n_iniciais > 10):
    print('O número máximo de estados inicias é 10')
    exit()

#Quantidade de estados de aceitação + estados de aceitação (uma linha)
aceitacao = input()
estados_aceitacao = aceitacao.split()
n_estados_aceitacao = int(estados_aceitacao[0])
estados_aceitacao.pop(0)
estados_aceitacao = list(estados_aceitacao)

#Quantidade de transições
n_transicoes = int(input())
if (n_transicoes > 50):
    print('O número máximo de transições é 50')
    exit()

#Inicializando listas (para múltiplos estados q') para cada símbolo de cada estado
for estado in af.keys():
    for simbolo in simb_terminais:
        af[estado][simbolo] = []

#Transições
tem_arco_lambda = 0
for x in range(n_transicoes):
    transicao = input()
    transicao = transicao.split()
    estado_inicial = transicao[0]
    simbolo = transicao[1]
    estado_final = transicao[2]
    af[estado_inicial][simbolo].append(estado_final)

# print("Antigos estados inicial: {}\nAntigos estados de aceitacão: {}\nAntigas transições:".format(list(range(n_iniciais)), estados_aceitacao))
# print(pprint.pformat(af))

#>>>> CONVERTER EM AFD
novos_estados = []
novo_inicial = ''

#definir novo estado inicial
for est_inicial in range(n_iniciais):
    novo_inicial += str(est_inicial)

if (novo_inicial not in af):
    novos_estados.append(novo_inicial)

#tratar arcos lambda
if '-' in simb_terminais:
    #estado origem e destino se referem a origem e destino de cada arco lambda
    for estado_origem in list(af.keys()):
        destinos_lambda = af[estado_origem]['-']    #todos os estados alcançáveis com uma ou mais transição lambda

        #para cada destino de lambda
        for estado_destino in destinos_lambda:
            destinos_lambda.extend(af[estado_destino]['-'])    #adiciona as transições lambda do destino às transições lambda da origem

            for simb in af[estado_destino]:
                af[estado_origem][simb].extend(af[estado_destino][simb])  #adiciona as transições 'simb' do destino lambda às transições 'simb' da origem
                af[estado_origem][simb].extend(af[estado_destino]['-'])   #adiciona as transições lambda do destino lambda
                
                #se houver transição 'simb' para o próprio estado, adiciona o destino lambda a transição 'simb' da origem 
                if estado_origem in af[estado_origem][simb]:
                    af[estado_origem][simb].extend(destinos_lambda)

            #se o destino do arco lambda for estado de aceitação, o estado origem tbm é
            if estado_destino in estados_aceitacao:
                estados_aceitacao.append(estado_origem)

        #adiciona à transição 'simb' do estado_origem os destinos das transições lambdas do estado_destino
        for simb in list(af[estado_origem].keys()):
            destinos_simb = af[estado_origem][simb]
            
            for destino_simb in destinos_simb:
                af[estado_origem][simb].extend(af[destino_simb]['-'])

    #apagar arcos lambda e remover repetições
    for estado in list(af.keys()):
        del af[estado]['-']

        for simb in list(af[estado].keys()):
            af[estado][simb] = list(set(af[estado][simb]))

    # print('\nTransições após tratar arcos-lambda:')
    # print(pprint.pformat(af))

#para estados com mais de uma transição com mesmo simbolo terminal,
#cria novo estado sendo a junção deles
for estado in af.keys():
    for simb in af[estado].keys():
        if len(af[estado][simb]) > 1:
            novo_estado = ''.join(sorted(af[estado][simb])) #junta todos os elementos da lista, ordenados (para evitar duplicações)
            novos_estados.append(novo_estado)
            af[estado][simb] = novo_estado

#definir transições dos novos estados
for novo_estado in novos_estados:
    af[novo_estado] = {}

    for simb in simb_terminais:
        destino = ''

        #cada digito de novo_estado é um antigo_estado.
        for antigo_estado in list(novo_estado):

            #se o antigo_estado tem transição para simb,
            if (simb in af[antigo_estado]):

                #para cada transição do estado antiga,
                #adiciona ao destino do novo estado
                for antigo_dest in af[antigo_estado][simb]:
                    if (antigo_dest not in list(destino)):
                        destino += antigo_dest

        #ordena o destino para evitar duplicação (ex: '01' e '10')
        sorted_destino = sorted(destino)
        destino = ''.join(sorted_destino)

        af[novo_estado][simb] = destino

        #se o destino gerado não existir ainda,
        #colocar na lista para gerá-lo
        if (destino not in af) and (destino != ''):
            novos_estados.append(destino)

#tirar elementos das listas
for estado in list(af.keys()):
    for simb in list(af[estado].keys()):
        elem = af[estado][simb]

        if isinstance(elem, list):
            #se a lista tiver mas de 1 elemento, remove
            if len(elem) > 1:
                #del af[estado][simb]
                break
            #se tiver só 1 elemento, coloca como string
            elif len(elem) == 1:
                af[estado][simb] = af[estado][simb][0]
            else:
                del af[estado][simb]

        #remove se for vazio
        elif (af[estado][simb] == ''):
            del af[estado][simb]

#definir novos estados de aceitação
for estado in af.keys():
    for c in list(estado):
        if c in estados_aceitacao and estado not in estados_aceitacao:
            estados_aceitacao.append(estado)

# print("\nNovo estado inicial: {}\nNovos estados de aceitacão: {}\nNovas transições:".format(novo_inicial, estados_aceitacao))
# print(pprint.pformat(af))

#Quantidade de cadeias a serem testadas
n_cadeias = int(input())
if (n_cadeias > 10):
    print('O número máximo de cadeias de entrada é 10')
    exit()

#testando para cada cadeia
for i in range(n_cadeias):
    cadeia = input().strip()
    # print(cadeia)

    if (len(cadeia) > 20):
        print('O comprimento máximo de cada cadeia é 20')
        exit()

    processed = 0
    estado = novo_inicial

    if cadeia == '-':
        cadeia = ''

    #Percorrendo os estados
    for x in cadeia:
        if x in af[estado]:
            #print("{}: from {} to {}".format(x, estado, af[estado][x]))
            estado = af[estado][x]    #Trocando o estado
            processed += 1
        else:
            break

    #Verificando se o estado final é o de aceitação
    #print("{} in aceitacao and {} == {}".format(estado, processed, len(cadeia.strip())))
    if (estado in estados_aceitacao) and (processed == len(cadeia)):
        #Se o estado final for de aceitação, não é necessário testar para os outros estados iniciais
        print("aceita")
    else:
        print("rejeita")