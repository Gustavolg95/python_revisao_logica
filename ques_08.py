print('Sequência de Fibonacci')

n = int(input('Quantos termos deseja ver? '))

print(f'\nSequência de Fibonacci com {n} termos:')

a, b = 0, 1
termos = []

for i in range(n):
    termos.append(a)
    a, b = b, a + b

print(', '.join(map(str, termos)))