# coding: utf8

class alumno:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self, num):
        self.edad = num