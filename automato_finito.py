#af é o dicionário que será utilizado para percorrer os estados do automato
af = {}

#Quantidade de estados
n_estados = int(input())
for x in range(n_estados):
    af[x] = {}

#Quantidade de símbolos terminais + símbolos terminais (uma linha)
terminais = input()
simb_terminais = terminais.split()
n_simb_terminais = simb_terminais[0]
simb_terminais.pop(0)

#Quantidade de estados iniciais
#AFD = 1, estado_inicial = q0
#AFN = n (n > 1), estado_inicial = [q0, q1, ..., qn]
n_iniciais = int(input())

#Quantidade de estados de aceitação + estados de aceitação (uma linha)
aceitacao = input()
estados_aceitacao = aceitacao.split()
n_estados_aceitacao = int(estados_aceitacao[0])
estados_aceitacao.pop(0)
estados_aceitacao = list(map(int, estados_aceitacao))

#Quantidade de transições
n_transicoes = int(input())

#Transições
for x in range(n_transicoes):
    transicao = input()
    transicao = transicao.split()
    estado_inicial = int(transicao[0])
    simbolo = transicao[1]
    estado_final = int(transicao[2])
    if simbolo not in af[estado_inicial]:
        af[estado_inicial][simbolo] = []
    af[estado_inicial][simbolo].append(estado_final)

print(af) 
# print(estados_aceitacao)
n_cadeias = int(input())

#Função pra verificar se cadeia é valida
def verificacao(af, cadeia, pos, estado):
    #Função recursiva  
    x = cadeia[pos]

    if x in af[estado]:
        if pos == len(cadeia) - 1:
            # if estado in estados_aceitacao: return 1
            for caminho in range(len(af[estado][x])):
                if af[estado][x][caminho] in estados_aceitacao:
                    return 1
            return 0
        else:
            for caminho in range(len(af[estado][x])):
                # print(af[estado][x][caminho])
                if verificacao(af, cadeia, pos + 1, af[estado][x][caminho]) == 1:
                    return 1
            return 0
    else:
        return 0

#Quantidade de cadeias a serem testadas
for i in range(n_cadeias):
    cadeia = input()

    #Testando para cada estado inicial
    for k in range(n_iniciais):
        if verificacao(af, cadeia, 0, k) == 1:
            print("aceita")
            break
        else:
            if k == n_iniciais - 1:
                print("rejeita")
        