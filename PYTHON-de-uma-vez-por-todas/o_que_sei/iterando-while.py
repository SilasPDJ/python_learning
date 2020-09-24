from time import sleep
nstring = ''
string = 'O rato roeu a roupa do Rei de Roma'
tString = len(string)

c = 0

while c < tString:
    if string[c].lower == 'r':
        nstring += string
    else:
        nstring += string[c]

    c += 1
for n in nstring:
    print(n, end='', sep='-')
    sleep(0.1)
# print(nstring)