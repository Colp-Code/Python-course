"""

Tipos de datos

Texto = str
Numerico = int, float, complex
Secuencia = list, tuple, range
Mapa = dict
conjunto = set, frozenset
booleano = bool
binario = bytes, bytearray, memoryview
ninguno = NoneType

"""

q = 5
print(type(q))
##  Con la función Type() se puede saber que tipo de dato tiene una variable

w = "Hello World"
e = 20
r = 20.5
t = 1j
y = ["apple", "banana", "cherry"]
u = ("apple", "banana", "cherry")
i = range(6)
o = {"name" : "John", "age" : 36}
p = {"apple", "banana", "cherry"}
a = frozenset({"apple", "banana", "cherry"})
s = True
d = b"Hello"
f = bytearray(5)
g = memoryview(bytes(5))
h = None

print(type(w))
print(type(e))
print(type(r))
print(type(t))
print(type(y))
print(type(u))
print(type(i))
print(type(o))
print(type(p))
print(type(a))
print(type(s))
print(type(d))
print(type(f))
print(type(g))
print(type(h))
#
#   Y puedes estableser el tipo de valor de una variable si pones 
# 
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))