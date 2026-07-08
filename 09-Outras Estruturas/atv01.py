'''Faça um código que receba 2 listas e encontre os elementos em comum.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
elm_comum= []
if len(a) > len(b):
  for i in range(len(a)):
    if a[i] in b:
        elm_comum.append(a[i])
  print(elm_comum)
if len(a) < len(b):
  for i in range(len(b)):
    if b[i] in a:
        elm_comum.append(b[i])
  print(elm_comum)