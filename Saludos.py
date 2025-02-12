#coding: utf-8
'''
Autor: Fernando Salas
Fecha: 12/02/2025
'''

nombre = input("Escriba su nombre: ")
lista = []

while nombre.upper() != "SALIR":
    lista.append(nombre)
    nombre = input("Escriba su nombre (o 'SALIR' para terminar): ")

for i in lista:
    print("Hola", i.capitalize())
    total = len(i)
    a = i.lower().count("a")
    print((round(a*100/total,2)))
