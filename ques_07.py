print('Informe um numero e descubra sua classificação')

n = int(input('Informe um numero inteiro: '))

print(f'O numero {n} eh:')
if n % 2 == 0:
    print(f'-PAR.')
else:
    print(f'-IMPAR.')

if n > 0:
    print(f'-POSITIVO.')
elif n < 0:
    print(f'-NEGATIVO.')
else:
    print(f'-ZERO.')

if n < 2:
    print('-NÃO É PRIMO')
else:
    eh_primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            eh_primo = False
            break
    if eh_primo:
        print('-PRIMO')
    else:
        print('-NÃO É PRIMO')