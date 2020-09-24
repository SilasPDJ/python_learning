"""
While / Else
Aula 8
contadores
acomuladores
"""
contador = 1
acumulador = 1
tf = [True, False]
quebra = tf[1]
while contador <= 10:
    print(contador, acumulador)
    if quebra and contador > 5:
        break

    acumulador += contador
    contador += 1
else:
    # SÓ EXISTE SE O WHILE RETORNAR FALSO,
    # QUANDO ELE PASSA A SER MAIOR QUE 10 POR EX
    print('Cheguei no else')
print('Aqui tá fora do else')