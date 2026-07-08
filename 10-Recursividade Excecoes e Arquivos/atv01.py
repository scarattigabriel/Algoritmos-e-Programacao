'''A Torre de Hanói é um problema matemático que consiste de três pinos (A, B e C) e um número n de discos empilhados em ordem de tamanho onde o menor disco fica por cima. O objetivo do problema consta em mover a pilha de discos do pino A para o pino C, respeitando as seguintes regras:

Apenas um disco pode ser movido por vez.
Um disco maior nunca pode ficar sobre um disco menor.
Implemente uma função recursiva torre_hanoi(n, origem, destino, auxiliar) que resolva o problema para n discos. A função deve imprimir cada movimento necessário.'''

def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mover disco {n} de {origem} para {destino}")
    torre_hanoi(n - 1, auxiliar, destino, origem)

# Teste com 2 discos
torre_hanoi(2, 'A', 'C', 'B')
print()
# Teste com 3 discos
torre_hanoi(3, 'A', 'C', 'B')
print()
# Teste com 4 discos
torre_hanoi(4, 'A', 'C', 'B')
print()