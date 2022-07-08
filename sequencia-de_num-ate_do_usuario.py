# Atividade 01
#Faça um proĀrama que peça um número maior que 1 ao usuário.
#Em seĀuida, imprima todos os números, de 1 até o número que o usuário inÿormou.

num = int (input(' Digite um numero maior que 1: '))
ini = 1
while ini <= num:
    print(ini)
    ini += 1
else:
    print('Fim do while.')