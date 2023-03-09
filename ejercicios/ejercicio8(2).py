import pickle

class Vehículo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

vehículo = Vehículo("Ford", "Mustang", 2022)

# Guardamos el objeto vehículo en un archivo
with open("vehículo.pickle", "wb") as archivo:
    pickle.dump(vehículo, archivo)

# Cargamos el objeto vehículo desde el archivo
with open("vehículo.pickle", "rb") as archivo:
    vehículo_cargado = pickle.load(archivo)

print("Marca:", vehículo_cargado.marca)
print("Modelo:", vehículo_cargado.modelo)
print("Año:", vehículo_cargado.año)
