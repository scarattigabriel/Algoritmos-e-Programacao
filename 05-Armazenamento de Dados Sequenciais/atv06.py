'''A cantina da UFFS e o RU fazem uma promoção semanal de descontos para clientes de acordo com as iniciais do nome da pessoa.

Crie um algoritmo que leia o primeiro nome do cliente, o valor de sua conta e se o nome do cliente iniciar com as letras A, D, S ou B o cliente terá um desconto de 30%.

Para o cliente cujo nome não se inicia por nenhuma dessas letras, exibir a mensagem "Que pena. Nesta semana o desconto não é para seu nome, mas continue nos prestigiando e comprando que sua vez chegará em breve".'''

lista_nome=[]
nome=input("Digite seu primeiro nome: ")
conta=float(input("Digite o valor da sua conta: "))
if nome[0].upper() in "ADSB":
  conta-= conta*0.30
  print(f"Você recebeu um desconto de 30% e sua conta ficou: {conta}")
else:
  print("Que pena. Nesta semana o desconto não é para seu nome, mas continue nos prestigiando e comprando que sua vez chegará em breve")