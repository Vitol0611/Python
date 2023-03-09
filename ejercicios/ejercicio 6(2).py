# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:10:56 2023

@author: victo
"""

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def resultado(self):
        if self.nota >= 5:
            print("El alumno", self.nombre, "ha aprobado.")
        else:
            print("El alumno", self.nombre, "ha suspendido.")

# Crear un objeto de la clase Alumno y llamar a sus métodos
alumno1 = Alumno("Juan", 7)
alumno1.imprimir_datos()
alumno1.resultado()
