# INTRODUÇÃO À PROGRAMAÇÃO - Lista de Execícios - Aula 03

#1) Crie um programa em Python que imprima uma mensagem que você ama programar com esta linguagem.
nome = input('Por favor, digite seu nome: ')
print(f"Olá! Sou {nome} e amo programar em Python!")

#2) Crie um programa em Python que pergunte o nome do usuário e imprima um bom dia com o nome do usuário.
#Dica: você pode utilizar o método .format() ou uma concatenação de string, por exemplo.
nome = input('Por favor, digite seu nome: ')
print(f"Olá, Sr(a). {nome}, bom dia!")

#3) Crie um programa em Python que solicite um número do usuário, depois some este número com 1357, multiplique
#por 8, divida por 5 e eleve ao quadrado.

numero = float(input('Por favor, digite um número: '))
numero = numero + 1357
numero = numero * 8
numero = numero / 5
numero = numero ** 2
total = numero
print("O total é:", total)

#4) Crie um programa em Python que imprima um convite para uma festa com o nome do usuário que for digitado.
#O nome do usuário precisará ser apresentado todo em caixa alta.

nome = input('Por favor, digite seu nome: ')
print("_____________________________________________________________________________________________________")

print(f"                 Olá, {nome.upper()}! :) \n"
"\n"
            "É com muito prazer que convido você para o meu aniversário! \n"

           "Te espero para juntos comemorar-mos essa data tão especial. \n"
"\n"   
      "                DATA: HORÁRIO: LOCAL: \n")

print("_____________________________________________________________________________________________________ \n")

#5) Crie um programa em Python em que as quatro operações em que todos os resultados resultam em 8.

print("Multiplicação")
multiplicacao = (2 * 4)
print(multiplicacao , "\n")

print("Divisão")
divisao = (32 / 4)
print(divisao, "\n")

print("Soma")
soma = (4 + 4)
print(soma, "\n")

print("Subtração")
subtracao = (12 - 4)
print(subtracao)
