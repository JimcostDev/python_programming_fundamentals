import threading
import requests
import time

urls = ["https://example.com"] * 10
lock = threading.Lock()  # Para evitar que los prints se solapen

def descargar(url):
    with lock:
        print(f"[+] Descargando {url} en el hilo {threading.current_thread().name}")
    response = requests.get(url)
    with lock:
        print(f"[{response.status_code}] Descarga de {url} completada")

# Versión secuencial
print("\n=== Ejecución Secuencial ===")
inicio_secuencial = time.time()

for url in urls:
    descargar(url)

tiempo_secuencial = time.time() - inicio_secuencial
print(f"Tiempo secuencial: {tiempo_secuencial:.2f} segundos\n")

# Versión concurrente
print("\n=== Ejecución Concurrente con Hilos ===")
inicio_concurrente = time.time()

hilos = []
for url in urls:
    hilo = threading.Thread(target=descargar, args=(url,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

tiempo_concurrente = time.time() - inicio_concurrente
print(f"\nTiempo concurrente: {tiempo_concurrente:.2f} segundos")
print(f"Speedup: {tiempo_secuencial/tiempo_concurrente:.1f}x")