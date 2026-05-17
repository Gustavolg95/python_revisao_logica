print('Vamos calcular o seu IMC!')

peso = float(input('Digite o seu peso, em KG: '))
altura = float(input('Digite a sua altura, em METROS: '))
IMC = peso / altura**2

if IMC < 18.5:
    print(f'Voce esta abaixo do peso, {IMC:.2f}Kg')

elif IMC < 25:
    print(f'Voce esta no peso ideal, {IMC:.2f}Kg')

elif IMC < 30:
    print(f'Voce esta no sobrepeso, {IMC:.2f}Kg')

elif IMC < 35:
    print(f'Voce esta em Obesidade grau I, {IMC:.2f}Kg')

elif IMC < 40:
    print(f'Voce esta em Obesidade grau II, {IMC:.2f}Kg')

else:
    print(f'Voce esta em Obesidade grau III, {IMC:.2f}Kg')