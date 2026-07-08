'''Exercício 12: qual será o valor impresso pelo programa abaixo? Faça um teste de mesa (tabela) e veja o resultado final da variável soma.'''

soma = 10
for i in range(8, 0, -3):
    soma -= i
    for j in range(1, i, 2):
        soma += j
print(soma)

##resposta: o valor impresso pelo programa será 10, pois a variável soma é inicializada com o valor 10 e, ao longo do loop, os valores de i e j são subtraídos e adicionados à variável soma, resultando no valor final de 10.