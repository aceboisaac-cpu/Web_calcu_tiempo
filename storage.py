import json
import os
import streamlit as st

# Archivo para persistencia de datos
DATA_FILE = "datos.json"

# Función para cargar datos desde el archivo
def cargar_datos():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, Exception):
            return {}
    return {}

# Función para guardar datos al archivo
def guardar_datos():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(st.session_state.bloques, f, indent=4, ensure_ascii=False)