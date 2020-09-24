cont = 0
tn = int(input('Quantos números deseja testar? '))

while cont < tn:
    while True:
        try:
            n = int(input(f'Digite o {cont+1}º número inteiro: '))
            break
        except ValueError:
            print('ERRO! Digite um número inteiro.')
    if n % 2 == 0:
        print(f'O número {n} é PAR')
    else:
        print(f'O número {n} é ÍMPAR')
    cont += 1
print(f'Você testou {cont} números')