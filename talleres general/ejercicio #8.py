import math

"""
entradas=
lado1=>float=>a
lado2=>float=>b
lado3=>float=>c
salida=
area=>float
"""
a=float(input("escribir lado _1 "))
b=float(input("escribir lado_2 "))
c=float(input("escribir lado_3 "))

s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area del triangulo : "+str(area))
