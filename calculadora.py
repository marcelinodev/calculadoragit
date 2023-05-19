

operador = float(input('Seleccione numero 1, 2, 3, 4: '))
if operador == 1:
    print('sumar')
elif operador == 2:
    print('resta')
elif operador == 3:
    print('multiplicar')
elif operador == 4:
    print('dividir')
else:
    print('seleccione nuebamente')

num1 = input('Primer numero: ')
num2 = input('segundo numero: ')
resultado = operador
print('Este es el total', resultado)


'''def suma(a, b):
    suma = (num1 + num2)
    return resultado
print(suma(5, 15))'''