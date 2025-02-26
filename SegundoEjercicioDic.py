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
    nombreAlumno = nombreAlumno.capitalize()  # Asegurar formato correcto
    numAsignaturas = int(input("Dime el número de asignaturas a registrar: "))
    diccionario = {}

    for i in range(numAsignaturas):
        nombreAsignatura = input("Dime el nombre de la asignatura: ")
        notaAsignatura = int(input("Dime la nota de esa asignatura: "))
        diccionario[nombreAsignatura] = notaAsignatura  # Guardar correctamente

    tupla = (nombreAlumno, diccionario)  # Guardar todo el diccionario, no solo la última materia
    lista.append(tupla)

    nombreAlumno = input("Dime el nombre de un alumno: ")

asignaturaMedia = input("Dime el nombre de la asignatura a conocer su media: ")

notas = []
for alumno in lista:
    if asignaturaMedia in alumno[1]:  # Verificar que la asignatura exista
        notas.append(alumno[1][asignaturaMedia])

if notas:
    print(f"Media de {asignaturaMedia}: {sum(notas) / len(notas)}")
else:
    print(f"No hay datos para la asignatura {asignaturaMedia}")
