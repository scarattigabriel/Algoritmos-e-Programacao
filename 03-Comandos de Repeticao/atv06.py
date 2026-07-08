'''Em um parque, uma árvore da espécie A tem 1,50m e cresce 2 cm por ano. Já uma árvore da espécie B tem 1,10m e cresce 3 cm por ano. Faça um programa que calcule quantos anos serão necessários para que a árvore B atinja a altura da árvore A.'''

a=150
b=110
contador= 0
while a != b:
 a += 2
 b += 3
 contador+=1
print(f"Serão necessários {contador} anos para que a árvore A atinja a altura de B")