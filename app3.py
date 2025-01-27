import streamlit as st
import random
import json

# Función para cargar los datos de teorías
def cargar_teorias():
    with open("teorias.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Función para mostrar la teoría y el ejemplo aleatorio
def mostrar_aleatorio():
    teorias = cargar_teorias()
    seleccion = random.choice(teorias)
    st.subheader(f"Teoría: {seleccion['teoria']}")
    st.write(f"Descripción: {seleccion['descripcion']}")
    st.write(f"Ejemplo de la vida diaria: {seleccion['ejemplo']}")

# Interfaz de la web
st.title("Teoría del Electromagnetismo con Ejemplo Cotidiano")
st.button("Mostrar Aleatorio", on_click=mostrar_aleatorio)
