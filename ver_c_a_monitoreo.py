import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Definir nombres de columnas para el DataFrame
column_names = ["aqi", "idx", "attributions", "city", "dominentpol", "iaqi", "time", "forecast", "debug"]

# Cargar los datos desde el archivo CSV
df = pd.read_csv('c_a_monitoreo.csv', names=column_names)

# Asegurarnos de que los datos están bien cargados
print(df.head())

# Revisar las primeras entradas de la columna 'time' para ver el contenido
print(df['time'].head())

# Extraer el campo 'iso' de la columna 'time' y convertirlo a datetime
def extract_iso_time(time_str):
    try:
        # Intentar cargar como JSON
        time_dict = json.loads(time_str.replace("'", '"'))  # Reemplazar comillas simples por comillas dobles
        return time_dict['iso']
    except json.JSONDecodeError:
        # Si falla, devolver la cadena directamente (asumir que ya es una cadena de tiempo)
        return time_str

df['time'] = df['time'].apply(extract_iso_time)
df['time'] = pd.to_datetime(df['time'], errors='coerce')

# Filtrar filas con NaT en la columna 'time'
df = df.dropna(subset=['time'])

# Asegurarnos de que los datos están bien convertidos
print(df['time'].head())

# Visualizar los datos de AQI
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='time', y='aqi')
plt.title('Índice de Calidad del Aire (AQI) en Medellín')
plt.xlabel('Tiempo')
plt.ylabel('AQI')
plt.show()