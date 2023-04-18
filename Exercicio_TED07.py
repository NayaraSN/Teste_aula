# INTRODUÇÃO À PROGRAMAÇÃO - Lista de Exercícios Aula 07 - TED 07
# Exercícios de fixação - Nível fácil ao intermediário

# 1. Fácil: Faça um programa que leia dois números inteiros e exiba o maior deles.

# num1 = 10
# num2 = 20
#
# if num1 > num2:
#     print(f"O maior número é {num1}")
# else:
#     print(f"O maior número é {num2}")


# 2. Fácil: Escreva um programa que receba a idade de uma pessoa e informe se ela é maior de idade ou não.

# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Você está na maioridade")
# else:
#     print("Você está na menoridade")


# 3. Fácil: Crie um programa que solicite o nome e a idade do usuário e informe se ele pode dirigir um veículo.

# nome = input("Digite o seu nome: ")
# idade = int(input("Digite a sua idade: "))
#
# if idade >= 18:
#     print(f"Que bom {nome}, você pode dirigir!")
# else:
#     print(f"Que pena {nome}, você não pode dirigir!")


# 4. Fácil: Faça um programa que calcule a média aritmética de 4 notas e informe se o aluno foi aprovado
#(média maior ou igual a 7) ou reprovado.

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# nota4 = float(input("Digite a quarta nota: "))
#
# media = (nota1 + nota2 + nota3 + nota4)/4
#
# if media >= 7:
#     print(f"Sua média é {media :.2f} e você está aprovado!")
# else:
#     print(f"Sua média é {media :.2f} e você está reprovado!")


# 5. Fácil: Escreva um programa que receba um número inteiro e informe se ele é par ou ímpar.

# numero = int(input("Digite um número: "))
#
# if numero % 2 == 0:
#     print(f"O número {numero} é par")
# else:
#     print(f"O número {numero} é ímpar")


# 6. Intermediário: Faça um programa que leia o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1500,00, o aumento é de 10%.
#Para salários inferiores ou iguais a R$1500,00, o aumento é de 15%.

# salario = float(input("Caro colaborador, digite o seu salário para saber seu aumento, R$ "))
#
# if salario > 1500:
#     print(f"O seu aumento foi de 10% totalizando {salario * 0.10 :.2f} reais, "
#           f"e seu novo salário é {(salario * 0.10) + salario :.2f} reais")
# else:
#     print(f"O seu aumento foi de 15% totalizando {salario * 0.15 :.2f} reais, "
#           f"e seu novo salário é {(salario * 0.15) + salario :.2f} reais")


# 7. Intermediário: Faça um programa que leia uma lista de números inteiros e informe qual o maior valor
#e qual o menor valor da lista.

# lista = [1, 2, 3, 4,5]
# print(f"O menor número da lista é {min(lista)}, e o maior é {max(lista)}")


# 8. Intermediário: Escreva um programa que leia uma string e verifique se ela é um palíndromo. Um palíndromo é uma
#palavra que pode ser lida tanto da esquerda para a direita quanto da direita para a esquerda e possui o mesmo significado.

frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
juntar = "".join(palavras)
inverso = juntar[::-1]
print(f"O inverso de {juntar} é {inverso}!")
if inverso == juntar:
    print("Temos um palíndromo!")
else:
    print("A frase não é um palíndromo, tente novamente!")


# 9. Intermediário: Faça um programa que gere a tabuada de um número informado pelo usuário.

# print("Vamos calcular a tabuada?")
# numero = int(input("Para isso, digite um número: "))
#
# print("-" * 30)
# print(f"Tabuada do {numero}:")
# for x in range(1, 11):
#     print(f"{numero} x {x} = {numero * x}")
# print("-" * 30)


# 10. Intermediário: Escreva um programa que leia uma lista de nomes e remova todos os nomes duplicados,
#deixando apenas um de cada nome na lista final.

# nomes = ["Nayara", "Edilson", "Edilson", "Maria", "Fátima", "Nayara", "Maria"]
# print("A lista inicial é:")
# for i in nomes:
#     print(i)
# print()
# print("A lista final é:")
# correcao = sorted(set(nomes))
# for i in correcao:
#     print(i)


