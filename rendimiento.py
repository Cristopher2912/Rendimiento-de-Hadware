import psutil
import time

def obtener_rendimiento_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Uso de CPU: {cpu_percent}%")

while True:
    obtener_rendimiento_cpu()
    time.sleep(1)
