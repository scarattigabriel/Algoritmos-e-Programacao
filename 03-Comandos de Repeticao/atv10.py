'''Num campeonato da Atlética Geral da UFFS de volleyball, se inscreveram 3 cursos. Sabendo-se que na lista oficial de cada curso consta, além de outros dados, a massa e a idade de 3 jogadores, criar um programa que apresente as seguintes informações:

1- A massa média e a idade média de cada um dos times.

2- A massa média e a idade média de todos os participantes.'''

cursos= 3
jogadores=3
acumulador_media_massa=0
acumulador_media_idade=0
for i in range(cursos):
    acumulador_massa=0
    acumulador_idade=0
    nome_curso= (input(f"Digite qual o nome do curso {i+1}/{cursos}: "))
    for i in range(jogadores):
        massa=int (input(f"Digite a massa do jogador {i+1}/{jogadores}: "))
        idade=int(input(f"Digite a idade do jogador {i+1}/{jogadores}: "))
        acumulador_massa += massa
        acumulador_idade += idade
    media_massa= acumulador_massa / jogadores
    media_idade= acumulador_idade / jogadores
    acumulador_media_massa += media_massa
    acumulador_media_idade += media_idade
    print(f"A idade média dos jodadores do curso {nome_curso} é: {media_idade} e a média de massa é: {media_massa}")
media_geral_massa= acumulador_media_massa / cursos
media_geral_idade= acumulador_media_idade / cursos
print(f"A média geral de idade é: {media_geral_idade} e a média geral de massa é: {media_geral_massa}")