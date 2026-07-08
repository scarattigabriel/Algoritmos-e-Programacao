'''Escreva uma função que realiza a correção de uma prova objetiva com 10 questões. A função deve receber duas listas, a primeira contendo o gabarito e a segunda contendo as respostas de um determinado aluno. A função deve retornar o número de acertos.

Chame a função passando as listas como parâmetro e exiba o número de acertos.

Exemplo de gabarito: [A, B, A, C, B, D, E, A, A, C]
''' '''
def corretor(gabarito, gabarito_aluno):
  acertos=0
  for i in range (10):
    if gabarito[i] == gabarito_aluno[i]:
      acertos+=1
  return acertos'''

def corretor(gabarito, gabarito_aluno):
    acertos = 0
    for i in range(10):
        if gabarito[i].upper() == gabarito_aluno[i].upper():
            acertos+=1 
    return acertos

gabarito=["A", "B", "A", "C", "B", "D", "E", "A", "A", "C"]
gabarito_aluno=[]
for i in range(10):
    respostas=(input("Digite a resposta: "))
    gabarito_aluno.append(respostas)
print(corretor(gabarito, gabarito_aluno))