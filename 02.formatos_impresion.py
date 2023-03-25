#FORMATOS DE IMPRESION
edad=31
estatura=1.62
print ("la edad es: ",edad)
print("la estatura es: ", estatura)
#1ra FORMA DE FORMATO:
print("La edad es:", edad,"y la estatura es", estatura)
#2da FORMA DE FORMATO: (La mas utilizada)
print(f'La edad es: {edad} y la estatura es: {estatura}')
#3ra FORMA DE FORMATO:
print('La edad es: {} y la estatura es: {}' .format(edad, estatura))
#ejemplos
print('La edad mas la estatura es:',edad+estatura)
print(f'La edad mas la estatura es:{edad + estatura}')
print('la edad mas la estatura es:{}' .format(edad+ estatura))
suma = edad + estatura
print(f'La edad mas la estatura es:{suma}')