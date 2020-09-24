import datetime
now = datetime.datetime.now()
atual = now.year


nome = str(input('Nome: '))
idade = int(input('Idade: '))

altura = float(input('Altura: '))

peso = float(input('Peso: '))


ano_nasc = atual - idade
imc = peso / (altura ** 2)

print(f'Olá, {nome}, você nasceu no ano de {ano_nasc}\n'
      f'Tem o peso {peso:.2f}, altura: {altura:.2f} e\n'
      f'IMC de {imc:.2f}')



