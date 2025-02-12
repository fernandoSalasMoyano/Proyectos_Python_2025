#coding utf-8
'''
Autor: Fernando Salas
Fecha: 29/01/2025
'''

x = int(input("Dame un primer número: "))
y = int(input("Dame un segundo número: "))

print("Suma: ", x+y)
print("Resta: ", x-y)
if(y!=0):
    print("División: ", x/y)
else:
    print("No se puede dividir por cero")
print("Multiplicación: ", x*y)