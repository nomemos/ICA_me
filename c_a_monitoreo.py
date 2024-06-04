import requests
import pandas as pd
import schedule
import time

# Configuración de la API
api_key = "651a4c6e7d43076656d685fad624655eb32cbf37"
city = "Medellín"
url = f"https://api.waqi.info/feed/{city}/?token={api_key}"

# Función para obtener datos de calidad del aire
def fetch_air_quality():
    response = requests.get(url)
    data = response.json()
    
    # Imprimir la respuesta completa para debugging
    print("Respuesta de la API:", data)
    
    if data["status"] == "ok":
        air_quality_data = data["data"]
        # Extraer el tiempo en un formato más simple
        air_quality_data['time'] = air_quality_data['time']['iso']
        df = pd.DataFrame([air_quality_data])
        df.to_csv('c_a_monitoreo.csv', mode='a', header=False, index=False)
        print(df)
    else:
        print("Error al obtener datos:", data.get("data", "No data"))

# Llamar a la función para obtener datos
fetch_air_quality()

# Programar para que se ejecute cada hora
schedule.every().hour.do(fetch_air_quality)

# Ejecutar el programa indefinidamente
while True:
    schedule.run_pending()
    time.sleep(1)