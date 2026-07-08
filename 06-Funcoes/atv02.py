'''Crie uma função que recebe o nome e sobrenome de uma pessoa, imprime uma mensagem "Bem vindo, fulano de tal!". Esta função não retorna nada. No programa principal, faça a leitura das duas strings e chame a função.'''

def bem_vindo(nome, sobrenome):
  print(f"Bem vindo, {nome} {sobrenome}")

nome=(input("Digite seu nome: "))
sobrenome=(input("Digite seu sobrenome: "))
bem_vindo(nome, sobrenome)