'''Exercício 3: pergunte a idade em anos do usuário e o classifique quanto a sua categoria etária (criança até 12 anos, adolescente dos 13 aos 17 anos, adulto dos 18 aos 64 anos ou idoso se mais de 64 anos). Se o usuário digitar um número negativo ou maior que 150 anos o programa deve imprimir uma mensagem de erro.'''

idade= int (input("Digite sua idade: "))
if idade >= 0 and idade <13:
  print("Criança")
elif idade >=13 and idade <18:
  print("Adolescente")
elif idade >=18 and idade <65:
  print("Adulto")
elif idade >= 65 and idade <=150:
  print("Idoso")
else:
  print("Erro")

idade= int(input("Digite sua idade: "))
if idade >=0 and idade<=150:
  if idade >= 0 and idade <13:
      print("Criança")
  else:
    if idade >= 13 and idade <18:
      print("Adolescente")
    else:
      if idade >=18 and idade < 65:
        print("Adulto")
      else:
        if idade >= 65 and idade <= 150:
          print("Idoso")
else:
  print("Erro")