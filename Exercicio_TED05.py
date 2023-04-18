# INTRODUÇÃO À PROGRAMAÇÃO - Lista de Exercícios Aula 06 - TED 05
# Estruturas de repetição

# 1. Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando
#divididos por 11, produzam o resto igual a 5.

# for numero in range(1000, 2001):
#    if (numero % 11) == 5:
#         print(numero)


# 2. Faça um programa que mostre as tabuadas dos números de 1 a 10.

# for x in range(1, 11):
#    print("_" * 20)
#    print()
#    print(f"Tabuada do {x}:")
#    for y in range(1, 11):
#        print(f"{x} x {y} = {x * y}")


# 3. Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada
#pessoa acessando cada elemento da lista um de cada vez.

# amigos = ("Junior", "Nayane", "Sara", "Yanka")
#
# for i in amigos:
#     print(i)


# 4. Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

# print("Vamos calcular a tabuada?")
# numero = int(input("Para isso, digite um número: "))
#
# print("-" * 30)
# print(f"Tabuada do {numero}:")
# for x in range(1, 11):
#     print(f"{numero} x {x} = {numero * x}")
# print("-" * 30)


# 5. Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado
#com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.

# amigos = ("Junior", "Nayane", "Sara", "Yanka")
#
# for i in amigos:
#     print(f"Olá {i}, como vai você?")
#     print()


# 6. Seja criativo ao desenvolver este programa.
# a) Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.

convidados = ["Rihanna", "Beyoncé", "Jenna Ortega", "Zendaya", "Harry Styles"]

print("Lista de convidados:")
for i in convidados:
  print(i)
print("_" * 110)

# b) Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.

print("Convites:")
for i in convidados:
    print(f"Olá {i}, gostaria de te convidar para um jantar sexta a noite na minha casa! ")
print("_" * 110)

# c) Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites.
#Imprima o nome das pessoas que não poderão comparecer.

convidado_ausente = [convidados.pop(2), convidados.pop(2)]
print("Os seguintes convidados não poderão comparecer:")
for i in convidado_ausente:
    print(i)
print("_" * 110)

# d) Modifique sua lista, substitua os desistentes por novos convidados.

convidados.insert(2, "Sia"), convidados.insert(3, "Shakira")
print("Nova lista de convidados:")
for i in convidados:
  print(i)
print("_" * 110)

# e) Exiba um novo convite para cada pessoa que continua presente em sua lista.

print("Novos convites:")
for i in convidados:
    print(f"Olá {i}, gostaria de te convidar para um jantar sexta a noite na minha casa! ")
print("_" * 110)


# 7. Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.

# while True:
#     nome = input("Digite seu nome: ")
#     print()
#     print(f"Olá Sr.(a) {nome}, seja bem vindo(a) a nossa central de cadastros!")
#     print("Sou a Rai e estou aqui para te ajudar!")
#     print()
#     idade = int(input("Digite sua idade: "))
#     email = input("Digite seu email: ")
#     if idade < 14:
#         print("Por favor verifique o campo idade e reinicie o cadastro.")
#         print("-" * 20)
#     else:
#         print("Dados confirmados!")
#         print()
#         print("Vamos criar seu login!")
#         usuario = input("Digite um nome de usuário: ")
#         senha = input("Digite uma senha: ")
#         print()
#         print("Casdastro concluído!")
#         print("Agradecemos a preferência!")
#         print("-" * 20)