import os
print('Descubra qual eh o tipo de triangulo, com base nos valores informados abaixo:')

A = float(input('Valor do lado "A": '))
B = float(input('Valor do lado "B": '))
C = float(input('Valor do lado "C": '))

if A + B > C and B + C > A and C + A > B:
    if A==B==C:
        print('Eh um Triangulo Equilatero, pois tem os tres lados com o mesmo comprimento.')

    elif A==B or A==C or B==C:
        print('Eh um Triangulo Isosceles, pois tem dois lados com o mesmo comprimento.')

    else:
        print('Eh um Triangulo Escaleno, pois tem os tres lados com comprimentos diferentes.')

else:
    print('Os valores informados nao formam um triangulo!')