'''Escreva um programa para ler o ano de fabricação de um veículo e informar ao usuário se ele é isento ou não do pagamento de IPVA.

Considere que o veículo se torna isento após 30 anos de sua fabricação.'''


ano_atual=2025
ano_fabricacao= int (input("Insira o ano de fabricação do veículo: "))
isencao= ano_atual - ano_fabricacao
if ano_atual - ano_fabricacao < 30:
  print("O seu veiculo não é isento de IPVA")
else :
  print ("O seu veículo é isento de IPVA")