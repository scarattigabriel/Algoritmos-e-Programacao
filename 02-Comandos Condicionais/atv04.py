'''Uma loja vende produtos à vista e a prazo. À vista é concedido um desconto de 5% e a prazo há um acréscimo de 10%.

Faça um programa que leia o preço do produto e a forma de pagamento. Depois, apresente o preço final do produto.'''

valor_produto= int (input ("Digite o valor do produto: "))
pagamento= int (input(f"Digite 1 para pagamento à vista e 2 para pagamentos à prazo: "))
if pagamento==1:
  valor_produto= (valor_produto/100)*95
  print(f"O valor do produto é {valor_produto}")
elif pagamento==2:
  valor_produto= (valor_produto /100)*110
  print(f"O valor do produto é {valor_produto}")
else:
  print("Erro")
