horario = 13

if 12 <= horario <= 17:
    print('Boa tarde!')

elif 0 <= horario < 12:
    print('Bom dia!')

elif 18 <= horario <= 24:
    print('Boa noite!')

else:
    print(f'{"Digite algo válido":~^30}')