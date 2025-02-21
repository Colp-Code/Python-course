import random
#   Hay tres tipo de numero en python
# Int
# Float
# Complex

q = 1   #Int
w = 1.2 #Float
e = 1j  #Complex

#   El tipo de dato Int es un numero entero ya sea positivo o negativo pero sin decimales de longitud ilimitada
#   Numeros Int o enteros

r = 1
t = 334343434343434
y = -12121212121212

print(type(r))#Int
print(type(t))#Int
print(type(y))#Int

#   Numeros float o flotante o condecimales

u = 1.1     
i = 1.0     
o = 1.11111 

print(type(u))  #Float
print(type(i))  #Float
print(type(o))  #Float

p = 35e3
a = 12E4
s = -87.7e100

print(type(p))  #Float o numero de Euler(De los numeros mas lindos)
print(type(a))  #Float
print(type(s))  #Float

# Numeros complejos
#   Los numeros complejos son escritos con una "j" como la parte imaginaria

d = 3+5j
f = 5j
g = -5j

print(type(d))
print(type(f))
print(type(g))

# Ahora convirtiremos unos tipos de numeros a otros
# Claro que el unico numero que no se puede convertir es el numero complejo

h = 1   #Int
j = 2.8 #Float
k = 1j  #Complex

l = float(h)
ñ = int(j)
z = complex(h)

print(l,ñ,z)

print(type(l))
print(type(ñ))
print(type(z))

#   Numero aleatorio

print(random.randrange(1,50))