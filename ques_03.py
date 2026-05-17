x = int(input('Digite um numero que queira saber a tabuada: '))

for i in range(1, 13):
    resposta = x * i
    print(f'{x} x {i} = {resposta}')