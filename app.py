import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Definir nombres de columnas para el DataFrame
column_names = ["aqi", "idx", "attributions", "city", "dominentpol", "iaqi", "time", "forecast", "debug"]

# Cargar los datos desde el archivo CSV
df = pd.read_csv('c_a_monitoreo.csv', names=column_names)

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

# Título de la aplicación
st.title('Visualización de Calidad del Aire')

# Mostrar el DataFrame en la aplicación
st.write(df)

# Visualizar los datos de AQI
st.subheader('Gráfico de AQI a lo largo del tiempo')
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='time', y='aqi')
plt.title('Índice de Calidad del Aire (AQI) en Medellín')
plt.xlabel('Tiempo')
plt.ylabel('AQI')
st.pyplot(plt)