'''Leia quatro números e imprima a média ponderada desses números, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.'''

nota1= int(input("Digite a primeria nota: "))
nota2= int(input("Digite a segunda nota: "))
nota3= int(input("Digite a terceira nota: "))
nota4= int(input("Digite a quarta nota: "))
media_ponderada= ((nota1*1)+(nota2*2)+(nota3*3)+(nota4*4))/10
print(f"A média ponderada das notas é {media_ponderada}")