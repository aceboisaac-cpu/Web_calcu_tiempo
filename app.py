
# Importamos Streamlit y la abrevia como "st"
import streamlit as st
import json
import os

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


# Función convertir segundos a sistema: h:m:s
def segundos_a_tiempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    return f"{horas:02}:{minutos:02}:{segundos_restantes:02}"


# Genera un H1 como título principal
st.title("Calculadora de tiempo por bloques.")

# Muestra una breve descripción de la app
st.write("Agregue sus bloques(días) y el tiempo que ocupa en cada tarea dentro del bloque, para calcular el tiempo total del bloque(día) y un promedio del tiempo total de sus bloques juntos(días de la semana).")

# Inicializar almacenamiento de bloques
if "bloques" not in st.session_state:
    st.session_state.bloques = cargar_datos()

#todo: SIDEBAR -> CREACIÓN DE BLOQUES
with st.sidebar:
    st.subheader("Crear Bloque")

    with st.form("form_bloque", clear_on_submit=True):

        nuevo_bloque = st.text_input("Nombre del Bloque")

        submitted = st.form_submit_button("Agregar bloque")

        if submitted:

            if nuevo_bloque and nuevo_bloque not in st.session_state.bloques:
                st.session_state.bloques[nuevo_bloque] = []
                guardar_datos()
                st.success(f"Bloque '{nuevo_bloque}' agregado correctamente")

            elif nuevo_bloque in st.session_state.bloques:
                st.warning("Este bloque ya existe")

            else:
                st.error("Debe ingresar un nombre")

# Apartado tipo H2 donde se muestren los bloques creados
st.subheader("Bloques de tareas:")

# Selector de bloque
bloque_seleccionado = st.selectbox(
    "Seleccione un bloque:",
    list(st.session_state.bloques.keys())
)

#todo Inputs de tiempo
with st.form("form_tiempo", clear_on_submit=True):

    col1, col2, col3 = st.columns(3)

    with col1:
        horas = st.number_input("Horas", min_value=0, max_value=23, step=1)

    with col2:
        minutos = st.number_input("Minutos", min_value=0, max_value=59, step=1)

    with col3:
        segundos = st.number_input("Segundos", min_value=0, max_value=59, step=1)

    submitted_tiempo = st.form_submit_button("Agregar tiempo")

    if submitted_tiempo:

        tiempo_total = horas * 3600 + minutos * 60 + segundos

        # Validar que el tiempo no sea 00:00:00
        if tiempo_total == 0:
            st.warning("Ingrese al menos horas, minutos o segundos")

        else:
            st.session_state.bloques[bloque_seleccionado].append(tiempo_total)
            guardar_datos()
            st.success("Tiempo agregado correctamente")
st.divider()


# Mostrar tiempos
st.subheader("Tiempos por bloque:")
for bloque, tiempos in st.session_state.bloques.items():
    st.write(f"Bloque: {bloque}")
    
    for i in range(0, len(tiempos), 4):
        fila = tiempos[i:i+4]
        cols = st.columns(4)

        for j, tiempo in enumerate(fila):
            with cols[j]:
                st.write(segundos_a_tiempo(tiempo))

                if st.button("ELIMINAR", key=f"del_{bloque}_{i+j}"):
                    st.session_state.bloques[bloque].pop(i+j)
                    guardar_datos()
                    st.rerun()

    # Total del tiempo de 1 bloque
    if tiempos:
        total = sum(tiempos)
        st.write(f"TOTAL: {segundos_a_tiempo(total)}")
    
    #? Eliminar bloques
    if st.button("ELIMINAR BLOQUE", key=f"del_block_{bloque}"):
        del st.session_state.bloques[bloque]
        guardar_datos()
        st.rerun()
    st.write("---")

#todo: SIDEBAR -> OPERACIONES
with st.sidebar:
    # Selector múltiple de bloques
    st.subheader("Operaciones globales")
    st.write("Al momento de crear y seleccionar sus bloques en este apartado:\n" \
    "\n1.- Se mostrará el total de tiempo de todos los bloques seleccionados.\n" \
    "\n2.- El promedio general de los bloques seleccionados.")
    bloques_seleccionados = st.multiselect(
        ("Seleccione Bloques"),
        list(st.session_state.bloques.keys())
    )
    # Calculo de la suma de bloques
    total_general = 0
    for bloque in bloques_seleccionados:
        total_general += sum(st.session_state.bloques[bloque])

    # Mostrar datos de suma y promedio
    if bloques_seleccionados:
        st.subheader("TOTAL GENERAL")
        st.write(segundos_a_tiempo(total_general))
        # Calculo del promedio de bloques
        cantidad = len(bloques_seleccionados)
        promedio = total_general / cantidad

        st.subheader("PROMEDIO")
        st.write(segundos_a_tiempo(int(promedio)))

#? Gráfica de datos
st.subheader("Gráfica de tiempo por bloque")

totales_bloques = {}

for bloque, tiempos in st.session_state.bloques.items():
    total_segundos = sum(tiempos)
    total_horas = total_segundos / 3600
    totales_bloques[bloque] = total_horas

if totales_bloques:
    st.bar_chart(totales_bloques)







