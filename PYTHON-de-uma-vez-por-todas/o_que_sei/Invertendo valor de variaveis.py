
x = 10 # Luiz
y = 'Luiz' # 10
"""
# mesma coisa abaixo
z = x
x = y
y = z
print(f'x={x} e y={y}')
"""


x, y = y, x
print(f'x={x} e y={y}')