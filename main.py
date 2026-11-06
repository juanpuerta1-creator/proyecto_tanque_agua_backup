from time import sleep
import sensor
import estado
import actuadores
import temperatura

bomba_encendida = "No activada" #la bomba inicia apagada
ciclos_limpieza = 0 #no hay ningun ciclo completado

while True:
    nivel_agua = sensor.medir_nivel()
    temperatura_agua = temperatura.medir_temperatura()

    if nivel_agua < 0:
        actuadores.apagar_bomba()
        actuadores.cerrar_valvula()
        print("Error de lectura. El sistema ha sido detenido por precaucion")
    elif nivel_agua < sensor.Nivel_Min:
        bomba_encendida = "Activada" #la bomba se enciende si el nivel del agua esta por debajo del limite
    elif nivel_agua > sensor.Nivel_Max:
        if bomba_encendida == "Activada":
            ciclos_limpieza = ciclos_limpieza + 1
            bomba_encendida = "No activada"

    if bomba_encendida == "Activada":
        actuadores.encender_bomba()
    elif bomba_encendida == "No activada":
        actuadores.apagar_bomba()

    if temperatura is not None:
        print(f"Temperatura del agua: {temperatura_agua:.1f} ºC")
    else:
        print("No se detecta el sensor de temperatura.")

    print(f"Nivel actual: {nivel_agua}% ----- Estado de la bomba: {bomba_encendida}")

    if ciclos_limpieza == estado.ciclos_maximo:
        print("Se han alcanzado los ciclos maximos. Se recomienda realizar una limpieza.")

    estado.mostrar_estado(nivel_agua)
