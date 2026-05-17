print('Calcule o valor do IPTU a ser pago:')

valor = float(input('Digite o valor do imóvel: R$ '))
tipo = str(input('Digite o tipo de imóvel "R", "C" ou "T": ')).upper()

if tipo == 'R':
    if valor <= 200000:
        v = 0.008 * valor
        print(f'O valor do IPTU a ser pago é R$ {v:.2f}')
    else:
        v = 0.012 * valor
        print(f'O valor do IPTU a ser pago é R$ {v:.2f}')

elif tipo == 'C':
    if valor <= 300000:
        v = 0.01 * valor
        print(f'O valor do IPTU a ser pago é R$ {v:.2f}')
    else:
        v = 0.015 * valor
        print(f'O valor do IPTU a ser pago é R$ {v:.2f}')

elif tipo == 'T':
    if valor <= 150000:
        v = 0.015 * valor
        print(f'O valor do IPTU a ser pago é R$ {v:.2f}')
    else:
        v = 0.02 * valor
        print(f'O valor do IPTU a ser pago é R$ {v:.2f}')

else:
    print('Tipo de imóvel inválido! Use R, C ou T.')