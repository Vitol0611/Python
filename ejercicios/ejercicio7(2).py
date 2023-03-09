import time

hora_actual = time.localtime().tm_hour
minutos_actuales = time.localtime().tm_min

if hora_actual >= 19:
    print("¡Es hora de ir a casa!")
else:
    hora_restante = 19 - hora_actual
    minutos_restantes = 60 - minutos_actuales
    tiempo_restante = hora_restante * 60 + minutos_restantes
    print("Quedan", tiempo_restante, "minutos de trabajo")
