# Simulador de Automato Finito

Trabalho da disciplina SCC0205 - Teoria da Computação e Linguagens Formais
Prof. João Luís Rosa
ICMC - USP

## Objetivo: 
Desenvolver o entendimento de Linguagens Formais e seu potencial de representação através
da implementação de simuladores de autômatos finitos.

## Entrada: 
* 1ª Linha: número de estados: para o conjunto de estados Q, assume-se os nomes dos
estados de q0 a qn−1, onde n é o número de estados, com 1 ≤ n ≤ 10;
* 2ª Linha: o conjunto de símbolos terminais (Σ): entrar com a quantidade de símbolos
terminais seguida dos elementos separados por espaçoo simples. Tamanho máximo igual a 10;
* 3ª Linha: o número de estados iniciais (Se for AFN, usa-se
q0, q1, etc. para os estados iniciais). Tamanho máximo igual a 10;
* 4ª Linha: o conjunto de estados de aceitação (F): entrar com a quantidade de estados
de aceitação seguida dos elementos separados por espaços. Entrar apenas com os números de 0 a 9;
* 5ª Linha: o número de transições (δ) da máquina. Quantidade máxima de 50;
* a partir da 6a Linha: as transições: entra-se com um δ em cada linha, com os elementos
separados por espaço: q x q0, onde q, q0 ∈ Q, x ∈ Σ ∪ {λ}. Represente a cadeia vazia
(λ) como “-”.
* Linha depois das transições: entrar com o número de cadeias de entrada (máximo de
10).
* Próximas Linhas: cadeias de entrada: entrar com uma em cada linha. Comprimento
máximo de cada cadeia = 20 símbolos.
