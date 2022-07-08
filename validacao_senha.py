senha = input(' Digite uma senha: ')
conf = input(' Digite novamante a senha: ')

while senha != conf:
    print('nao pode')
    senha = input(' Digite uma senha: ')
    conf = input(' Digite novamante a senha: ')
else:
    print('senha cadrastada')