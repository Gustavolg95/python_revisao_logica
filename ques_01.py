import math
pi = math.pi

print('Para calcular a volume de um cone, informe os valores abaixo:')
r = float(input('O valor para o raio: '))
h = float(input('O valor para a altura: '))
V = (1/3) * pi * r**2 * h

print(f'O volume do cone eh de: {V :.2f} metros.')
