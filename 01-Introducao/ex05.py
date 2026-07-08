'''Exercício 5: leia dois números inteiros, divida o primeiro pelo segundo e mostre os seguintes resultados, conforme formato abaixo.

Dividendo:
Divisor:                 
Quociente:              
Resto:
'''

dividendo=  int(input("Digite o dividendo: "))
divisor=  int(input("Digite o divisor: "))
quociente= dividendo/divisor
resto= dividendo%divisor
print(f"Dividendo: {dividendo}\nDivisor: {divisor}\nQuociente: {quociente:.2f}\nResto: {resto}")