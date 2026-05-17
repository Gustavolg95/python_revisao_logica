print('Descubra o seu desconto adquirido, com base no valor pago;')
r = float(input('Valor pago: R$'))

d = (r * (1 - 0.05))
if r <= 100:
    print('Você não ganhou nenhum desconto da compra!')
    if 100.1 > r <= 500:
        print('Você ganhou 10% de desconto!')
        print(f'O valor com desconto ficou {r * (1 - 0.10)}')

    elif r <= 1000:
        print('Você ganhou 15% de desconto!')
        print(f'O valor com desconto ficou {r * (1 - 0.15)}')

    elif r <= 5000:
        print('Você ganhou 20% de desconto!')
        print(f'O valor com desconto ficou {r * (1 - 0.20)}')

    elif r > 5000:
        print('Você ganhou 25% de desconto!')
        print(f'O valor com desconto ficou {r * (1 - 0.25)}')

else:
    print(f'O valor da sua compra foi de, R${r}')
    print(f'Mas a loja ainda oferece 5% de desconto adicional para pagamento a vista.')
    p = input('Digite "S" para sim ou "N" para não. Seu pagamento será à vista? ')
    if p == "S":
        print(f'Com o pagamento à vista, o valor será de R${r * (1 - 0.10)} reais.')
    else:
        print(f'O valor sem o desconto adicional, será de R${r} reais.')