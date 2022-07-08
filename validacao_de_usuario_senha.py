nome= input("Digite nome de usuario: ")
senha = input(' Digite uma senha: ')
while senha == nome:
    print('nao pode')
    nome = input("Digite nome de usuario: ")
    senha = input(' Digite uma senha: ')
else:
    print('usuario cadrastado')
