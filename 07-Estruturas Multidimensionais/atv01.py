'''Crie uma função que construa e retorne uma matriz conforme os parâmetros repassados. A função deve receber como parâmetro o número de linhas, o número de colunas e o valor padrão inicial da matriz.'''

def funcao_matriz (linhas, colunas, vp):
  matriz=[]
  for i in range(linhas):
    linha=[]
    for j in range(colunas):
        linha.append(vp)
    matriz.append(linha)
  return matriz

linhas=int(input("Digite o número de linhas: "))
colunas=int(input("Digite o número de colunas: "))
vp=int(input("Digite o valor padrão: "))

funcao_matriz(linhas,colunas, vp)