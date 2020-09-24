def make_list_v2(ing):
    ingsplt = ing.split('0')
    ingsplt.pop(0)
    newt = list()
    # UNWANTED
    for elem in ingsplt:
        elem = f'0{elem}'
        newt.append(elem)
    return newt


def make_list(ing):
    # wanted
    splt = ing.split('0')
    splt.pop(0)
    new = [f'0{v}' for v in splt]
    return new


def point(ing):
    # wanted
    splt = ing.split('0')
    splt.pop(0)
    new = [f'0{v}' for v in splt]
    new = '.'.join(new)
    return new

numeros = list(range(0, 10))
print(numeros)
numeros_str = str(numeros)[1:-1]
numeros_str = numeros_str.replace(',', '').replace(' ', '')

times = 7
string = ''
for i in range(times):
    string += numeros_str

mklis = make_list(string)
print(mklis)

final = point(ing=string)
print(final)
