string = [olha for isso in range(3) for olha in list(range(0, 10))]
neww = [str(s) for i in range(3) for s in string]

print(neww)

j_string = ''.join(neww)
print(j_string)

n = 10
comprehension = [j_string[i:i+n] for i in range(0, len(j_string), n)]
print(comprehension)

joinit = '.'.join(comprehension)
print(joinit)
