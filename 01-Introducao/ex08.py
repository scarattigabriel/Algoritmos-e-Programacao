'''Exercício 8: observe o exemplo abaixo e defina a ordem de avaliação dos operadores no código seguinte.'''
x = 1
y = 2
resultado = x > 0 or not x == y and x + y == 5
print(resultado)
'''# Substituíndo variáveis na expressão
# 1 > 0 or not 1 == 2 and 1 + 2 == 5

# Avaliando operadores aritméticos
# 1 + 2 = 3
# 1 > 0 or not 1 == 2 and 3 == 5

# Avaliando operadores relacionais
# 1 > 0 = True
# True or not 1 == 2 and 3 == 5

# 1 == 2 = False
# True or not False and 3 == 5

# 3 == 5 = False
# True or not False and False

# not False = True
# True or True and False

# True and False = False
# True or False = True
# O resultado final da expressão é True
'''