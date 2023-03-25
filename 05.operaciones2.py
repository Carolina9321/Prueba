# OPERACIONES RELACIONALES O DE COMPARACION ****
#True(1) / false(0)
number = int(input('Digite un numero: '))
print(number > 3)  # el numero es mayor a 3?
print(number >= 3)  # el numero es mayor o igual a 3?
print(number < 3)  # el numero es menor que 3?
print(number <= 3)  # el numero es menor o igual  que 3?
print(number == 3)  # el numero es igual que 3?
print(number != 3)  # el numero es diferente que 3?

#OPERACIONES LOGICAS***
print('Operaciones Logicas.')
# Conjuncion (and &)
# Arroja True cuando todas las entradas son True de lo contrario False
print('Conjuncion')
print(False and False and True)
print(False & False & True)
print(number > 3 & number < 10)

# Disyuncion (or |)
# Arroja True cuado una de sus entradas es True
print('Disyuncion')
print(False or False)
print(number <= 3 or number >= 10)
print(not (number <= 3 | number >= 10))

# Negacion (not)
print('Negacion:')
print(not (True))

# Or exclusiva (^)
# Va a ser falso cuando las dos entradas seas iguales
print('Or exclusiva:')
print(False ^ False)
print(True ^ False)
print(True ^ True)

#***OPERACIONES DE PERTENENCIA***
#in
print('Pertenencia- operador in')
nombre = 'Carolina Quimbayo'
print('Q' in nombre)
print('Z' in nombre)
