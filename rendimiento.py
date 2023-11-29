import psutil
import time

def obtener_rendimiento_cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Uso de CPU: {cpu_percent}%")

while True:
    obtener_rendimiento_cpu()
    time.sleep(1)

import subprocess

def ping_ip(ip_address):
	command = ['ping', '-c', '4', ip_address]
	result = subprocess.run(command, capture_output=True, text=True)
	print(result.stdout)

ip_address = '10.3.21.194'
ping_ip(ip_address)
