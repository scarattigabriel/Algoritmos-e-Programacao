'''Exercício 5: uma loja possui um estoque de um determinado produto e deseja monitorar suas vendas até que o estoque acabe. Crie um algoritmo que peça para o usuário informar a quantidade inicial de estoque e faça um laço que pergunte quantas unidades foram vendidas até que o estoque acabe. Use o comando break para encerrar o laço de repetição quando o estoque chegar em zero e então imprima uma mensagem para o usuário de estoque esgotado. Valide também a entrada do usuário quanto a venda, esta não deve ser maior que o estoque disponível. Use o comando continue para repetir a entrada do usuário se este for o caso sem debitar nada do estoque.
Observe que com o uso dos comandos continue e break não é necessário usar comandos condicionais em cascata para resolver esse exercício.'''

estoque= int(input("Estoque inicial: "))
while True:
  vendas=int(input("Número de produtos vendidos: "))
  if vendas > estoque:
    print("Digite outro valor!Estoque indisponível")
    continue
  estoque-= vendas
  print("Estoque atual: ", estoque)
  if estoque==0:
    print("Estoque esgotado!")
    break