"""
Funções built-in len, abs, type, print, etc...

built-in: embutidas
"""
texto = 'Python s2'

print(texto[-len(texto):-3])
extencao = texto[:2].lower()
print(extencao)

url = 'google.com.br/'
print(url[:-1])

t = list()
for i in range(97, 123):
    t.append(chr(i))
for e, abc in enumerate(t):

    print(abc.upper(), end=' ', sep='')
    if (e+1) % 3 == 0:
        print('...')