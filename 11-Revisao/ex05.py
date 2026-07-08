'''Exercício 5: Crie uma função que receba uma string como parâmetro e retorne a quantidade de vogais (a, e, i, o, u) que essa string possui.'''
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

texto = "Computador"
resultado = contar_vogais(texto)
print(resultado)
# Saída esperada: 4