'''Exercício 1: usando os comandos condicionais solicite para o usuário o ano, mês e dia de seu nascimento (use três variáveis para armazenar os valores) e, usando os comandos condicionais, calcule e imprima a sua idade em anos.'''

ano_atual=int (input("Digite o ano atual: "))
dia_atual=int (input("Digite o dia atual: "))
mes_atual=int (input("Digite o mês atual: "))
ano_nascimento= int (input("Digite o ano do seu nascimento: "))
mes_nascimento= int (input("Digite o mês de seu nascimento: "))
dia_nascimento= int (input("Digite o dia do seu nascimento: "))
idade= ano_atual - ano_nascimento
if (ano_nascimento > 0 and ano_nascimento < 2026) and (mes_nascimento > 0 and mes_nascimento <= 12) and (dia_nascimento > 0 and dia_nascimento <= 31):
  if mes_nascimento > mes_atual or (mes_nascimento == mes_atual and dia_nascimento > dia_atual):
    idade= idade-1
  print(f"Sua idade é: {idade}")
else:
  print ("Data inválida")