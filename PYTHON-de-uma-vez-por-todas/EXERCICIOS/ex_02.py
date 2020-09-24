hora = input('Digite um orário (0-23): ')
if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Horário deve estar entre 0 e 23 horas')
    elif hora <= 11:
        print('Bom dia!')
    elif hora <= 17:
        print('Boa tarde!')
    else:
        print('Boa noite!')

else:
    print('Por favor, digite um horário entre 0 e 23.')
