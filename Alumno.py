class Alumno:
    def __init__(self, nombre, dicNotas):
        self.nombre = nombre
        self.dicNotas = dicNotas

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setAsignatura(self, nombreAsignatura, notaAsignatura):
        self.dicNotas[nombreAsignatura] = notaAsignatura
    
    def getAsignaturas(self):
        return self.dicNotas

    def getNota(self, nombreAsignatura):
        return self.dicNotas[nombreAsignatura]
    
    def setNota(self, nombreAsignatura, notaAsignatura):
        self.dicNotas[nombreAsignatura] = notaAsignatura
    
    def getMedia(self):
        import statistics
        return statistics.mean(self.dicNotas.values())

    #    cantidad = len(self.dicNotas)
     #   sumatorio = 0
      #  for i in self.dicNotas.values():
       #     sumatorio += i
        #return sumatorio/cantidad