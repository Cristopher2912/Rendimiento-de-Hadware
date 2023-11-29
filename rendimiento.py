import psutil

# Obtener la cantidad de memoria disponible
memoria_disponible = psutil.virtual_memory().available / (1024 * 1024)

# Obtener el porcentaje de uso de la memoria
memoria_usada = psutil.virtual_memory().percent

# Obtener el rendimiento de la red
rendimiento_red = psutil.net_io_counters().bytes_sent / (1024 * 1024)

# Obtener la temperatura del CPU (solo disponible en algunas plataformas)
try:
temperatura_cpu = psutil.sensors_temperatures()['coretemp'][0].current
except AttributeError:
temperatura_cpu = "No disponible en esta plataforma"

# Imprimir la cantidad de memoria disponible, el porcentaje de uso de la memoria, el rendimiento de la red y la temperatura del CPU
print(f"Memoria disponible: {memoria_disponible:.2f} MB")
print(f"Porcentaje de uso de la memoria: {memoria_usada:.2f}%")
print(f"Rendimiento de la red: {rendimiento_red:.2f} MB")
print(f"Temperatura del CPU: {temperatura_cpu}")



import subprocess
import psutil
import time

def ping_ip(ip_address):
    command = ['ping', '-c', '4', ip_address]
    result = subprocess.run(command, capture_output=True, text=True)
    print(f"Tiempo de respuesta para la IP {ip_address}:")
    for respuesta in result.stdout.splitlines():
        if not respuesta.strip().startswith("Ping"):
            continue
        tiempo_de_respuesta = float(respuesta.split()[5])
        print(f"Tiempo de respuesta: {tiempo_de_respuesta} segundos")

def obtener_rendimiento_cpu(ip_address):
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Uso de CPU para la IP {ip_address}: {cpu_percent}%")

ips = ["10.3.21.194", "10.3.21.195", "10.3.21.196", "10.3.21.197"]

for ip in ips:
    ping_ip(ip)
    obtener_rendimiento_cpu(ip)
    time.sleep(1)


