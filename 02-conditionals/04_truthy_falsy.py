# Valores falsy
if []:
    print("No se ejecuta")

if "":
    print("No se ejecuta")

if 0:
    print("No se ejecuta")

# Valores truthy
if [1, 2, 3]:
    print("Se ejecuta")  # ✓

if "hola":
    print("Se ejecuta")  # ✓

if 42:
    print("Se ejecuta")  # ✓

# Uso común
lista = []
if lista:
    print("La lista tiene elementos")
else:
    print("La lista está vacía")  # ✓
