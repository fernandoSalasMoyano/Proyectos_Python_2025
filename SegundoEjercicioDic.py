'''
Crear un programa que lea por teclado el nombre de un alumno, lea cuantas asignaturas se van a guardar y para cada una de ellas guarde 
el nombre de la asignatura y la nota correspondiente. Se dejara de leer datos cunado el nombre dle alumno sea "Salir"
en cualquier forma escrita

Para almacenar los datos, usaremos una lista de tuplas con el nombre del alumno (en formato correcto) y un diccionario formado por 
los pares Nombre de la asignatura : nota del alumno

Calcular la media de una asigantuara común para todos los alumnos.
'''

nombreAlumno = input("Dime el nombre de un alumno: ")
lista = []

while nombreAlumno.upper() != "SALIR":
    numAsignaturas = int(input("Dime el número de asignaturas a registrar: "))

    for i in range(numAsignaturas):
        nombreAsignatura = input("Dime el nombre de la asignatura: ")
        notaAsignatura = int(input("Dime la nota de esa asignatura: "))
        tupla = (nombreAlumno, {nombreAsignatura:notaAsignatura})
        lista.append(tupla)
    nombreAlumno = input("Dime el nombre de un alumno: ")

asignaturaMedia = input("Dime el nombre de la asignatura a conocer su media: ")

print(lista)
notas = []
notasTotal = 0
for i in range(len(lista)):
    notas.append(lista[i][1][asignaturaMedia])
    notasTotal = notasTotal + notas[i]

print("Media de ", asignaturaMedia, ": ", notasTotal/len(lista))