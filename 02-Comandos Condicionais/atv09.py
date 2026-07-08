'''Adapte o programa abaixo mudando a expressão booleana do segundo comando if. Ao invés de usar o operador and na expressão booleana, mude a expressão para usar o operador or mantendo o mesmo comportamento lógico.

idade = int(input("Digite a sua idade: "))
if idade >= 16:
    if idade >= 18 and idade < 70:
        print("Você pode votar e é obrigado a votar")
    else:
        print("Você pode votar, mas não é obrigado a votar")
else:
    print("Você não pode votar")
'''
idade = int(input("Digite a sua idade: "))
if idade >= 16:
    if idade <18 or idade > 70:
        print("Você pode votar, mas não é obrigado a votar")
    else:
        print("Você pode votar e é obrigado a votar")
else:
    print("Você não pode votar")