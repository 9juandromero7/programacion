"""
entradas=
edad1=>int=>(e1)
edad2=>int=>(e2)
edad3=>int=>(e3)
salidas=
promedio=>float=>prom
"""

e1=int(input("escriba su edad"))
e2=int(input("escriba su edad"))
e3=int(input("escriba su edad"))

prom=(e1+e2+e3)/3
print("su promedio de edad es: "+str(prom))