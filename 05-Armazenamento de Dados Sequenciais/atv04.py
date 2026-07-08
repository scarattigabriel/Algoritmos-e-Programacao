'''Faça um código que receba cria uma lista com alguns números e peça para o usuário um número que ele deseja remover.

Imprima a lista após a remoção desse número ou, caso não esteja presente na lista, avise o usuário com uma mensagem.'''

lista= [0,1,2,3,4,5,6,7,8,9]
elemento_remocao=int(input(f"Digite quais elementos deseja remover da lista : {lista}"))
if elemento_remocao in lista:
  while elemento_remocao in lista:
    lista.remove(elemento_remocao)
  print(lista)
else:
  print("Elemento não presente na lista!")