'''Faça um programa que leia a idade de uma pessoa e a classifique em menor ou maior de idade. Antes de passar para a classificação, deve ser verificado se a idade está no intervalo entre 0 e 120. Em caso negativo, o programa deve repetir a leitura de dados até que um valor dentro deste intervalo seja digitado.'''

while True:
  idade=int(input("Digite sua idade: "))
  if idade < 0  or idade > 120:
    print("Digite um valor válido!")
    continue
  elif idade < 18:
    print("Menor de idade!")
  else:
    print("Maior de idade!")
  break