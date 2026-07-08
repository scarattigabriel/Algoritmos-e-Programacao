'''Crie uma função que dadas duas matrizes A e B de mesmo tamanho, retorne uma nova matriz que é a soma de A e B.'''

def sum_matriz (matriz_a, matriz_b):
  matriz_final= []
  for j in range(2):
    matriz=[]
    for i in range(len(matriz_a[0])):
      soma=0
      soma= matriz_a[j][i] + matriz_b[j][i]
      matriz.append(soma)
    matriz_final.append(matriz)
  return matriz_final

a=[[6,1,7], [2,5,9]]
b=[[4,3,2], [1,2,3]]
print(sum_matriz(a,b))