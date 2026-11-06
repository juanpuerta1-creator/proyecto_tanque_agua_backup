from machine import Pin
from time import sleep_ms
import onewire
import ds18x20

# Configuracion del sensor de temperatura
pin_temperatura = Pin(4)

# Comunicacion OneWire
bus = onewire.OneWire(pin_temperatura)

# Inicializacion del DS18B20
sensor_temperatura = ds18x20.DS18X20(bus)

# Buscar el sensor conectado
sensores = sensor_temperatura.scan()


def medir_temperatura():

    if len(sensores) == 0:
        return None

    # Solicitar una nueva medicion
    sensor_temperatura.convert_temp()

    # Esperar la conversion
    sleep_ms(750)

    # Obtener temperatura en grados Celsius
    temperatura = sensor_temperatura.read_temp(sensores[0])

    return temperatura
