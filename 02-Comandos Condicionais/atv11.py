'''Faça uma nova versão da atividade acima de modo que, caso os 3 valores formem um triângulo, o programa informe também qual o seu tipo: equilátero, isósceles ou escaleno.'''

a= int (input("Digite um valor inteiro: "))
b= int (input("Digite um valor inteiro: "))
c= int (input("Digite um valor inteiro: "))
if a + b > c or a + c > b or b + c > a:
  print("Os valores representam lados de um triângulo")
  if a == b == c:
    print("Triângulo equilátero")
  elif a == b != c or a == c != b or b == c != a:
    print("Triângulo isósceles")
  else: print("Triângulo escaleno")
else:
  print("Os valores não representam lados de um triângulo")