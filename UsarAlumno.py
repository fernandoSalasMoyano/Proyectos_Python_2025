import Alumno

alumno1 = Alumno.Alumno("Fernando", {})

print(alumno1.getNombre())
alumno1.setAsignatura("Matematicas", 9)
alumno1.setAsignatura("Geografía", 3)
alumno1.getNota("Matematicas")

print(alumno1.getMedia())