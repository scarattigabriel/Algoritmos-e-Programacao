'''Use a função input() para ler de um usuário as informações de um produto adquirido. Crie uma variável para armazenar o nome do produto, outra para o valor unitário (converta para o tipo float) e mais uma para a quantidade adquirida (converta para o tipo int). Compute o valor total da compra e depois use apenas uma chamada da função print() para imprimir os dados conforme o exemplo de saída abaixo (os números reais devem ser formatados para apresentarem 2 casas decimais).

O nome do produto adquirido é tenis, o seu valor unitário é R$499.90 e foram adquiridas 2 unidades, totalizando uma compra de R$999.80.
'''
produto= input("Insira o nome do produto: ")
valor_unitario= float(input("Insira o valor unitário do produto: "))
quantidade_produto= int(input("Insira a quantidade do produto: "))
valor_total= valor_unitario*quantidade_produto
print(f"O nome do produto adquirido é {produto}, o seu valor unitário é {valor_unitario:.2f} e foram adquiridas {quantidade_produto} unidades, totalizando uma compra de {valor_total:.2f}")