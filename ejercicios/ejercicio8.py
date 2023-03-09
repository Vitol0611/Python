# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:35:28 2023

@author: victo
"""

archivo = open("archivo.txt", "w")

archivo.write("Primera escritura\n")
archivo.close()

archivo = open("archivo.txt", "a")
archivo.write("Segunda escritura\n")
archivo.close()
