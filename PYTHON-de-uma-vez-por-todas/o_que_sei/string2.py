my_list = list(range(10)) * 5
# print(my_list)
string = ''
for f in my_list:
    string += str(f)

n = 10

lista = [string[i:i+n] for i in range(0, len(my_list), 10)]
print(lista)
lista_junta = '.'.join(lista)
print(lista_junta)