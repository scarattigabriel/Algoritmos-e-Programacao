'''Exercício 3: Crie uma classe que represente um veículo. O veículo deve conter os atributos: marca, modelo e ano. Crie uma instância de exemplo para ilustrar o uso da classe com o veículo: marca "Toyota", modelo "Corolla", ano 2020 e eletrico "Não".'''

class Veiculo:
    marca = None
    modelo = None
    ano = None
    eletrico = None

    def __init__(self, marca, modelo, ano, eletrico):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.eletrico = eletrico

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"É elétrico: {self.eletrico}")


carro = Veiculo(marca="Toyota", modelo="Corolla", ano=2020, eletrico="Não")
carro.exibir_informacoes()