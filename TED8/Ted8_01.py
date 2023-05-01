# INTRODUÇÃO À PROGRAMAÇÃO - TED 08
# Vetores e Matrizes

# 1.  Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20
#números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

import random

vetor = [] * 20

for i in range(20):
    vetor.append(random.randint(0, 20))
print(vetor)
print()
inverso = vetor[::-1]
print("Os números digitados em ordem inversa são: ")
print(inverso)

