#Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia, e R$ 1,00 se
#forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas,
#calcule e escreva o custo total da compra.

n_macas= float(input("Digite a quantidade de maças compradas: "))

if n_macas < 12:
    n_macas = n_macas * 1.30
    print(f" O custo total da compra é {n_macas} reais")

else:
    n_macas = n_macas * 1.00
    print(f" O custo total da compra é {n_macas} reais")
