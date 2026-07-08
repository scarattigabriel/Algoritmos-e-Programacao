'''Faça um programa que leia um número inteiro e exiba True se este número é múltiplo de 4 e de 3 simultaneamente, ou False caso contrário.'''

numero= int (input("Digite um número: "))
print(f"O número {numero} é múltiplo de 3 e 4 simultaneamente: { numero % 4 == 0 and numero % 3 == 0}")