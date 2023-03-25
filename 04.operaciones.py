#OPERACIONES ARITMETICAS
#suma,resta, multp,div /,div entera //,residuo o modulo %,potencia**.
#Jerarquia: (), **,*/.+ -
number = int(input('digite un numero: '))
'''print(f'La suma con 2 es: {number + 2}')
print(f'La resta con 2 es: {number - 2}')
print(f'La multiplicacion con 2 es: {number * 2}')
print(f'La division con 2 es: {number / 2}')
print(f'La division ENTERA con 2 es: {number // 2}')
print(f'El residuo con 2 es: {number % 2}')
print(f'La potencia con 2 es: {number ** 2}')'''

#operaciones de asignacion
contador = 1
contador += 1  # (+=) op. de asignacioon incremental
contador = 2
contador -= 1  # (-=) op. de asignacioon decremental

number += 1
print(f' Al usar operador incremental += el resultado es: {number}')
number -= 1
print(f' Al usar operados decremental -= el resultado es: {number}')
number *= 2
print(f' Al usar operados *= el resultado es: {number}')
number /= 2
print(f' Al usar operador /= el resultado es: {number}')
number //= 2
print(f' Al usar operador //= el resultado es: {number}')
number %= 2
print(f' Al usar operador %= el resultado es: {number}')
number **= 2
print(f' Al usar operador **= el resultado es: {number}')
