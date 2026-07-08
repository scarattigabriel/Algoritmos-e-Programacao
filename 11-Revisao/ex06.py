'''Exercício 6: Crie uma função que receba dois parâmetros: uma lista de números e um número inteiro chamado limite. A função deve retornar uma lista contendo apenas os números da lista original que sejam menores que o limite informado.'''

def filtrar_menores(lista, limite):
    resultado = []
    for numero in lista:
        if numero < limite:
            resultado.append(numero)
    return resultado

numeros = [5, 10, 15, 20, 25]
resultado = filtrar_menores(numeros, 18)
print(resultado)