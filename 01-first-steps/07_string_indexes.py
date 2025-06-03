"""
As in other languages, in Python String behave as
arrays, each letter or character is a position within the string.
"""

name = "Manuel"

print(name[0])
print(name[2])
print(name[-1])  # [-1] tomal el último elemento.

# [start:stop]
# Toma el inicio, y lo haya hasta antes del final, sin incluir el final.
print(name[0:3])


# [start:stop:stepover]
# Es lo mismo que antes, pero el stepover añade saltos según el número especificado.
# El valor por defecto del stepover es 1.
print(name[0:3:2])

# Ejercicio - String al revés
# Si dejo el start y stop vacíos, quiere decir que toma todo el string.
print(name[::-1])
