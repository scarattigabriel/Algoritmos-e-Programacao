'''Exercício 4: (Melhore o exercício anterior) Crie uma função na classe do Veículo chamada possui_imposto, que ao ser acionadao, retorne uma mensagem "Isento de imposto" caso o veículo possui 30 anos ou mais ou se for elétrico, ou a mensagem "Requer pagamento de 2% do imposto sobre o valor do veículo." caso o veículo for mais novo e não for elétrico.'''

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

    def possui_imposto(self):
        ano_atual = 2025
        idade = ano_atual - self.ano
        if idade >= 30 or self.eletrico.lower() == "sim":
            return "Isento de imposto"
        else:
            return "Requer pagamento de 2% do imposto sobre o valor do veículo."


carro = Veiculo(marca="Toyota", modelo="Corolla", ano=2020, eletrico="Não")
print(carro.possui_imposto())