# Los operadores lógicos nos ayudan a evaluar condiciones

# AND operator - evalua que todos los valores sean verdaderos
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# OR operator - evalua que al menos un valor sea verdadero
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# Negation
print(not True)  # False
print(not False)  # True

# AND
age = 25
is_licenced = True

if age >= 18 and is_licenced:
    print("Can drive")

# OR
is_student = False
has_membership = True

if is_student or has_membership:
    print("You can access premium resorces")

# Negation
is_admin = False

if not is_admin:
    print("Access denied")
