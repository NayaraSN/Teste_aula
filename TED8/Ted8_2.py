# INTRODUÇÃO À PROGRAMAÇÃO - TED 08
# Vetores e Matrizes

# 2. Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
#números repetidos no vetor VET e em que posições se encontram.

import random

vetor = [] * 10

for i in range(10):
    vetor.append(random.randint(0, 10))
print(vetor)
print()

repetidos = []
posicoes = []

for i in range(10):
    for j in range(i+1, 10):
        if vetor[i] == vetor[j] and vetor[i] not in repetidos:
            repetidos.append(vetor[i])
            print(f"O número {vetor[i]} se repete nas posições {i} e {j}")
            if len(repetidos) == 0:
                print("Não há números repetidos no vetor.")
