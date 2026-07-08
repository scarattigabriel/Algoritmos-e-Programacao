'''Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, crie um program que calcule e imprima o tempo necessario para que a população do pais A ultrapasse a população do pais B'''

pais_a= 5000000
pais_b= 7000000
while pais_a <= pais_b:
  pais_a*= 1.03
  pais_b*= 1.02
  contador+=1
print(f"São necessários {contador} anos para que o pais A ultrapasse a população do pais B")