'''Crie uma classe para representar um número complexo (possui dois atributos, parte real e imaginária. Implemente os métodos de adição, subtração e multiplicação na classe do número com outro número.

'''

class Complexo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        if self.imaginario >= 0:
            return f"{self.real} + {self.imaginario}i"
        else:
            return f"{self.real} - {abs(self.imaginario)}i"

    def __add__(self, other):
        return Complexo(self.real + other.real, self.imaginario + other.imaginario)

    def __sub__(self, other):
        return Complexo(self.real - other.real, self.imaginario - other.imaginario)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginario * other.imaginario
        imaginario = self.real * other.imaginario + self.imaginario * other.real
        return Complexo(real, imaginario)

# Testando a classe Complexo
c1 = Complexo(3, 4)
c2 = Complexo(5, -2)

# Soma
soma = c1 + c2
print("Soma:", soma)

# Subtração
subtracao = c1 - c2
print("Subtração:", subtracao)

# Produto
produto = c1 * c2