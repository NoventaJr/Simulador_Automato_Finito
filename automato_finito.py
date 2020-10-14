#Quantidade de estados
n_estados = int(input())

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
n_estados_aceitacao = estados_aceitacao[0]
estados_aceitacao.pop(0)

#Quantidade de transições
n_transicoes = int(input())

#Transições
for x in range(n_transicoes):
    transicao = input()
    transicao = transicao.split()
    estado_inicial = transicao[0]
    simbolo = transicao[1]
    estado_final = transicao[2]

#Criar dicionario de dicionarios

#Quantidade de cadeias a serem testadas
n_cadeias = int(input())
for i in range(n_cadeias):
    cadeia = input()

    #Testando para cada estado inicial
    for i in range(n_iniciais):
        #Percorrendo os estados
        for x in cadeia:
            print(dict[estado][x])      #Verificar se esta passando pelos estados corretamente, lembrar de apagar
            estado = dict[estado][x]    #Trocando o estado

        #Verificando se o estado final é o de aceitação
        if estado in estados_aceitacao:
            #Se o estado final for de aceitação, não é necessário testar para os outros estados iniciais
            print("aceita")
            break
        else:
            #Verificando se já percorreu todos os estados iniciais
            if i == n_iniciais - 1:
                print("rejeita")