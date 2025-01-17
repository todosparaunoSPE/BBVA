# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:42:16 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import plotly.express as px  # Para gráficos dinámicos
import random

# Configuración de la página
st.set_page_config(page_title="Manager de Cultura y Compromiso", layout="wide")


# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


# Instalar Faker si no está instalado
#st.text('Instalando Faker...')
#!pip install faker

# Crear una barra lateral con "Ayuda", nombre y copyright
st.sidebar.title("Ayuda")
st.sidebar.markdown("""
**¿Cómo usar esta aplicación?**

Esta aplicación simula una encuesta de compromiso laboral para 50 trabajadores de BBVA. Los resultados se visualizan en gráficos dinámicos.

1. **Distribución de Satisfacción**: Muestra cómo los empleados califican su satisfacción con el rol. Los empleados califican entre 1 y 10, y puedes ver cómo se distribuyen las respuestas.
2. **Reconocimiento**: Muestra cómo los empleados perciben el reconocimiento que reciben en la organización. Al igual que el punto anterior, los empleados califican entre 1 y 10.
3. **Oportunidades de Crecimiento**: Muestra cómo los empleados ven las oportunidades de crecimiento dentro de la empresa. La calificación varía entre 1 y 10, mostrando la percepción de los empleados.
4. **Nivel de Compromiso**: Se muestra cómo el nivel de compromiso varía según el rango de antigüedad de los trabajadores. Los empleados están agrupados en diferentes rangos de tiempo en la empresa.

**Propuestas de Valor para BBVA**

- **Reconocimiento y bienestar**: Crear programas de reconocimiento regular y promover el bienestar integral.
- **Desarrollo profesional**: Diseñar rutas claras de crecimiento y capacitaciones.
- **Comunicación efectiva**: Implementar canales de comunicación bidireccional para escuchar y actuar sobre el feedback.

**Cronograma de Iniciativas**

Un ejemplo de cronograma para implementar iniciativas clave sería:

- **Encuesta de Clima Laboral**: Iniciar en febrero de 2025 y finalizar en marzo de 2025.
- **Programa de Reconocimiento**: Comenzar en marzo de 2025 y terminar en junio de 2025.
- **Taller de Desarrollo**: Comenzar en abril de 2025 y finalizar en mayo de 2025.

**Autor: Javier Horacio Pérez Ricárdez**  
© 2025 Todos los derechos reservados.
""")

# Portada
st.title("Propuesta para Manager de Cultura y Compromiso - BBVA")
st.markdown("""
Esta aplicación presenta ideas clave y estrategias para fomentar la cultura organizacional y el compromiso en BBVA.
""")

# Sección: Encuesta de Compromiso
st.header("1. Encuesta de Compromiso (Simulación)")
st.markdown("""
Diseñar una encuesta para medir el nivel de compromiso laboral puede incluir preguntas como:
- ¿Qué tan satisfecho estás con tu rol actual?
- ¿Sientes que tu trabajo es valorado?
- ¿Consideras que hay oportunidades de crecimiento?

A continuación, puedes simular respuestas y visualizar los resultados:
""")

# Inicializar Faker para generar datos sintéticos
fake = Faker()

# Número de trabajadores
num_workers = 50

# Simulación de datos de encuesta para 50 trabajadores
worker_data = {
    "Nombre": [fake.name() for _ in range(num_workers)],
    "Satisfacción con el rol": np.random.uniform(1, 10, num_workers).round(2),  # Satisfacción con el rol
    "Percepción de reconocimiento": np.random.uniform(1, 10, num_workers).round(2),  # Reconocimiento
    "Oportunidades de crecimiento": np.random.uniform(1, 10, num_workers).round(2),  # Oportunidades de crecimiento
    "Nivel de compromiso": np.random.randint(1, 6, num_workers),  # Nivel de compromiso (1-5)
    "Fecha de contratación": [fake.date_this_decade() for _ in range(num_workers)]  # Fecha de contratación
}

# Crear DataFrame para trabajadores
df_workers = pd.DataFrame(worker_data)

# Mostrar todos los datos de los trabajadores (ahora se muestran los 50)
st.write(df_workers)

# Gráfico de distribución de las calificaciones con mayor separación entre las barras
fig_satisfaction = px.histogram(df_workers, x="Satisfacción con el rol", nbins=10, title="Distribución de Satisfacción con el Rol",
                                labels={"Satisfacción con el rol": "Calificación de Satisfacción (1-10)"})
fig_satisfaction.update_layout(bargap=0.3)  # Aumenta la separación entre barras
st.plotly_chart(fig_satisfaction)

fig_recognition = px.histogram(df_workers, x="Percepción de reconocimiento", nbins=10, title="Distribución de Percepción de Reconocimiento",
                                labels={"Percepción de reconocimiento": "Calificación de Reconocimiento (1-10)"})
fig_recognition.update_layout(bargap=0.3)  # Aumenta la separación entre barras
st.plotly_chart(fig_recognition)

fig_growth = px.histogram(df_workers, x="Oportunidades de crecimiento", nbins=10, title="Distribución de Oportunidades de Crecimiento",
                          labels={"Oportunidades de crecimiento": "Calificación de Oportunidades de Crecimiento (1-10)"})
fig_growth.update_layout(bargap=0.3)  # Aumenta la separación entre barras
st.plotly_chart(fig_growth)

# Gráfico de compromiso por rango de edad (ficticio)
df_workers['Rango de edad'] = pd.cut(df_workers['Fecha de contratación'].apply(lambda x: pd.to_datetime(x).year), 
                                     bins=[2010, 2015, 2020, 2025], labels=["10-15 años", "5-10 años", "0-5 años"])

fig_commitment = px.box(df_workers, x="Rango de edad", y="Nivel de compromiso", title="Nivel de Compromiso por Rango de Edad",
                        labels={"Nivel de compromiso": "Nivel de Compromiso (1-5)", "Rango de edad": "Años en la empresa"})
st.plotly_chart(fig_commitment)

# Sección de KPI´s
st.header("2. KPI´s Dinámicos")

# Función para actualizar aleatoriamente los KPI's
def simulate_kpi_update():
    return {
        "Prom. Satisfacción con el rol": round(random.uniform(6.5, 9.5), 2),
        "Prom. Reconocimiento": round(random.uniform(6.5, 9.5), 2),
        "Prom. Oportunidades de Crecimiento": round(random.uniform(6.5, 9.5), 2),
        "Prom. Compromiso": round(random.uniform(3.5, 4.5), 2),
    }

# Actualización de los KPI's con valores aleatorios
kpi_values = simulate_kpi_update()

# Muestra los KPIs en cuadros interactivos
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Prom. Satisfacción con el rol", f"{kpi_values['Prom. Satisfacción con el rol']} / 10", delta=f"{random.uniform(-1, 1):.2f}")
    
with col2:
    st.metric("Prom. Reconocimiento", f"{kpi_values['Prom. Reconocimiento']} / 10", delta=f"{random.uniform(-1, 1):.2f}")
    
with col3:
    st.metric("Prom. Oportunidades de Crecimiento", f"{kpi_values['Prom. Oportunidades de Crecimiento']} / 10", delta=f"{random.uniform(-1, 1):.2f}")
    
with col4:
    st.metric("Prom. Compromiso", f"{kpi_values['Prom. Compromiso']} / 5", delta=f"{random.uniform(-0.5, 0.5):.2f}")

# Sección: Propuestas de Valor para BBVA
st.header("3. Propuestas de Valor para BBVA")
st.markdown("""
Estrategias clave para fortalecer la cultura y el compromiso en BBVA:

- **Reconocimiento y bienestar**: Crear programas de reconocimiento regular y promover el bienestar integral.
- **Desarrollo profesional**: Diseñar rutas claras de crecimiento y capacitaciones.
- **Comunicación efectiva**: Implementar canales de comunicación bidireccional para escuchar y actuar sobre el feedback.

A continuación, se presentan ejemplos de cómo estas estrategias pueden impactar:
""")

# Simulación de KPI
kpi_data = {
    "Indicador": ["Satisfacción Laboral", "Retención de Empleados", "NPS Interno"],
    "Actual": [72, 85, 60],
    "Proyectado": [85, 90, 75]
}
df_kpi = pd.DataFrame(kpi_data)

# Crear gráfico de barras para el impacto proyectado en KPIs
fig_kpi = px.bar(df_kpi, x="Indicador", y=["Actual", "Proyectado"],
                 barmode="group", title="Impacto Proyectado en Indicadores Clave",
                 labels={"value": "Porcentaje (%)"}, color_discrete_sequence=["#636EFA", "#EF553B"])
st.plotly_chart(fig_kpi)

# Sección: Cronograma de Iniciativas
st.header("4. Cronograma de Iniciativas")
st.markdown("""
Un ejemplo de cronograma para implementar iniciativas clave sería:

- **Encuesta de Clima Laboral**: Iniciar en febrero de 2025 y finalizar en marzo de 2025.
- **Programa de Reconocimiento**: Comenzar en marzo de 2025 y terminar en junio de 2025.
- **Taller de Desarrollo**: Comenzar en abril de 2025 y finalizar en mayo de 2025.
""")
