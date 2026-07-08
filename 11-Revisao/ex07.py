'''Exercício 7: Crie uma função que recebe uma lista de nomes de pessoas e uma tupla com dois índices do tipo inteiro (posição inicial e posição final). A função deve retornar uma nova lista contendo apenas os nomes entre essas posições (inclusive o índice final).'''

def filtrar_nomes_intervalo(nomes, intervalo):
    # Acessando a tupla pelos índices 0 (início) e 1 (fim)
    inicio = intervalo[0]
    fim = intervalo[1]
    nomes_filtrados=[]
    for i in range(inicio, fim + 1):
        nomes_filtrados.append(nomes[i])
    return nomes_filtrados

# Lista
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
# Tupla
intervalo = (1, 3)

resultado = filtrar_nomes_intervalo(nomes, intervalo)
print(resultado)