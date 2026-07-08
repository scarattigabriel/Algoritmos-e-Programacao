'''Exercício 1: teste as conversões de diferentes valores e tipos para booleano. Identifique (baseado apenas nos seus testes) qual é o critério usado pela função bool() na conversão.'''

v_int = 5 # variável do tipo int
v_float = 5.6 # variável do tipo str
v_str = "7.87" # variável do tipo str
v_bool = True # variável do tipo bool
# imprime os valores das variáveis a, b, c e d
print(v_int)
print(v_float)
print(v_str)
print(v_bool)
print()
e = int(v_float)
print(e) #o valor original é truncado ao ser convertido para inteiro (apenas a parte inteira do número permanece)
e = int(v_bool)
print(e) # True sempre é convertido para o valor 1 enquanto False para o valor 0
e = int(False)
print(e)#0
#e = int(v_str) # a função não consegue converter diretamente o texto para inteiro pois o número é real
e = float(v_str) # primeiro converte o texto para float e depois para inteiro para funcionar
e = int(e)
print(e)
print(int(float(v_str))) # podemos compor funções para digitar menos linhas de código

print(bool(0)) # False somente quando zero
print(bool(-1))
print(bool(1))
print(bool(1.5))
print(bool("")) # False somente quando string vazia
print(bool(" "))
print(bool("texto"))
