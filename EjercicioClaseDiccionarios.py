#coding: utf-8
'''
Autor: Fernando Salas
Fecha: 12/02/2025
'''

tupla1 = ("matematicas", 8)
tupla2 = ("lengua", 9)

lista1 = [tupla1, tupla2]

alumnos = {"Fernando":lista1}
alumnos["Luis"] = [("matematicas", 4)]
print(alumnos)

for i in alumnos:
    print(i, alumnos[i][0][1]) # i(clave del diccionario) alumnos[i] el valor de esa clave
                                # alumnos[i][0] el primer elemento de la lista
                                # alumnos[i][0][1] el segundo elemento de la tupla