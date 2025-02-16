# ---------------------
#   Variables gobales
# ---------------------
q = "increible"

def myFunc():
    print("Python es",q)

myFunc()
# --------------------
#   Ejemplo de la variable local y de la variable global
# --------------------
w = "Porkio"

def mySecon():
    w = "Jhon"
    print("hola señor",w)
mySecon()

print("Hola señor",w)
# --------------------
# Palabra clave global
# --------------------
# Esto esta para crear una variable global en una función

def mythree():
    global e
    e = "fantastico"
mythree()

print("Python es",e)
# --------------------
#   Tambien se puede usar el keyword global para cambiar el valor de una variable global dentor de una funcion
# --------------------
r = "Pedro"
def myfour():
    global r
    r = "carlos"
myfour()
print("Hola",r)
