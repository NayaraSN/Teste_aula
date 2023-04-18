# INTRODUÇÃO À PROGRAMAÇÃO - Lista de Execícios - Aula 04
# Estruturas de seleção

# 1) Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou menor que 10.
#O programa deve escrever a mensagem correspondente (maior ou menor) e informar o valor digitado pelo usuário.

numero = int(float(input("Por favor digite um número: ")))
if numero > 10:
    print(f"{numero}, é maior que 10")
elif numero < 10:
    print(f"{numero}, é menor que 10")
else:
    print(f"{numero}, é igual a 10")


# 2)Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma
#mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior a 6 o aluno é aprovado).
#Escrever também o resultado da média calculada.

nota1 = float(input("Por favor digite a primeira nota: "))
nota2 = float(input("Por favor digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 6 and media <= 10:
    print("Aluno aprovado!"f" Sua média é {media}")
elif media < 6 and media >= 0:
    print("Aluno reprovado!"f" Sua média é {media}")
else:
    print("Valor incorreto!")


# 3) Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

valor1 = 1000
valor2 = -1000

if valor1 > valor2:
    print("O valor 1 é maior!")
else:
    print("O valor 2 é maior!")


# 4) Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor1 = 1000
valor2 = -1000

if valor1 > valor2:
    print(f"Menor: {valor2} | Maior: {valor1}")
else:
    print(f"Menor: {valor1} | Maior: {valor2}")


# 5) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e
#escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior
#ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

n_conta = 123456
saldo = 1000
debito = 999
credito = 150

saldo_atual = (saldo - debito) + credito

if saldo_atual >= 0:
    print(f"Seu saldo é R$ {saldo_atual} reais, e é positivo.")
else:
    print(f"Seu saldo é R$ {saldo_atual} reais, e é negativo.")


# 6) Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque
#de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
#Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão
#escrever a mensagem 'Efetuar compra'.

qtd_atual = 5456
qtd_max = 10000
qtd_min = 1000

qtd_media = int((qtd_max + qtd_min)/2)
print(f"A quantidade média é {qtd_media}")

if qtd_atual >= qtd_media:
    print("Não efetuar compra!")
else:
    print("Efetuar compra!")