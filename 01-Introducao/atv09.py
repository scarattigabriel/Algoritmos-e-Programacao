'''Faça um programa que compute as raízes da equação dada por ax² + bx + c = 0 sendo que a = 2, b = 14 e c = -60'''

a,b,c= 2, 14, -60
delta= (b**2 - 4*a*c)
x1= (-b + delta**(1/2))/(2*a)
x2= (-b - delta**(1/2))/(2*a)
print(f"Os valores de x1 e x2 são respectivamente: {x1} e {x2}")