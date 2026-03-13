# Conceptos de Arquitectura y Buenas Prácticas (Isaac's Project)

Este documento no es solo un manual, es tu **bitácora de aprendizaje**. Aquí explicamos el *porqué* de las decisiones de diseño que tomamos.

## 1. Modularización: La "Caja de Herramientas"
Pasamos de tener un solo archivo gigante ([app.py](file:///c:/Users/LAPTOP/Documents/ISAAC/CODE/PROYECTOS_CODING/Python/Web_calcu_tiempo/app.py)) a separar la **Persistencia** en [storage.py](file:///c:/Users/LAPTOP/Documents/ISAAC/CODE/PROYECTOS_CODING/Python/Web_calcu_tiempo/storage.py).

### El Concepto: Separación de Responsabilidades
- **app.py**: Se encarga de la **IU (Interfaz de Usuario)**. No debería saber CÓMO se guardan los datos, solo que existe una función que lo hace.
- **storage.py**: Se encarga de los **Datos**. Su único trabajo es leer y escribir en el disco.

> [!TIP]
> Si mañana quieres usar una Base de Datos SQL, solo tienes que modificar [storage.py](file:///c:/Users/LAPTOP/Documents/ISAAC/CODE/PROYECTOS_CODING/Python/Web_calcu_tiempo/storage.py). El archivo [app.py](file:///c:/Users/LAPTOP/Documents/ISAAC/CODE/PROYECTOS_CODING/Python/Web_calcu_tiempo/app.py) ni se enteraría del cambio. A esto se le llama **Bajo Acoplamiento**.

## 2. Git y el flujo de trabajo Profesional
Git no es solo para "hacer copias", es para **contar la historia** de tu código.

### Comandos Clave:
1. `git add .`: Pones tus cambios en la "sala de espera" (Staging Area).
2. `git commit -m "mensaje"`: Sacas la foto definitiva. El mensaje debe ser descriptivo (ej: `feat: modularizar persistencia`).
3. `git push`: Mandas tus fotos a la nube (GitHub).

> [!IMPORTANT]
> El [.gitignore](file:///c:/Users/LAPTOP/Documents/ISAAC/CODE/PROYECTOS_CODING/Python/Web_calcu_tiempo/.gitignore) es tu filtro de seguridad. Nunca subas entornos virtuales (`venv`) ni archivos de datos personales a la nube de forma pública.

## 3. Entornos Virtuales (`venv`)
Un `venv` es un **universo paralelo** para tu proyecto. 
- Evita que las librerías de un proyecto rompan las de otro.
- El archivo [requirements.txt](file:///c:/Users/LAPTOP/Documents/ISAAC/CODE/PROYECTOS_CODING/Python/Web_calcu_tiempo/requirements.txt) es la **receta** para que cualquier otro desarrollador pueda recrear tu universo en su compu.

## 4. Python vs Streamlit (Ejecución)
Aprendimos que no todos los programas de Python se ejecutan igual.
- `python app.py`: Ejecuta el script de arriba a abajo y termina.
- `streamlit run app.py`: Crea un **servidor web** que se queda escuchando cambios y dibuja la interfaz en el navegador.

---
*Documentación generada por Antigravity (Tu Senior de confianza).*
