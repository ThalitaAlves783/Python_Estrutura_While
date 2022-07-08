num = int (input(' Digite um numero entre 0 e 10: '))

while num > 10 or num < 0:
    print('digite novamente numero errado')
    num = int(input(' Digite um numero entre 0 e 10: '))
else:
    print('correto')