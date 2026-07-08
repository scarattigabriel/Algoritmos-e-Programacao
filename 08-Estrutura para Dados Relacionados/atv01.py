'''
Crie uma lista com 3 carros (objetos da classe Carro), faça a leitura dos dados e, ao final, imprima os dados dos 3 carros.'''

class Carro:
    modelo = None
    marca = None
    ano = None
    cor = None
loja = [] 
for i in range(3):
    car = Carro()
    car.modelo = input("Digite o modelo do carro: ")
    car.marca = input("Digite a marca do carro: ")
    car.ano = input("Digite o ano de fabricação do carro: ")
    car.cor = input("Digite a cor do carro: ")
    loja.append(car)

print("\nRelatório de carros da loja:")
for carro in loja:
    print("   marca: ",carro.marca, " modelo: ", carro.modelo, " ano: ", carro.ano, " cor: ", carro.cor)