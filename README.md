# 📊 Análisis del Uso de Redes Sociales y su Impacto en la Ansiedad

Este proyecto tiene como objetivo explorar, limpiar y analizar datos recolectados a través de una encuesta sobre el uso de redes sociales. Posteriormente, entrena un modelo de machine learning para predecir niveles de ansiedad en función del comportamiento digital.

---

## 🧠 Objetivo

- Explorar cómo el tiempo de uso, red social más utilizada, hora de conexión y otros factores se relacionan con la ansiedad.
- Entrenar un modelo de predicción usando algoritmos de aprendizaje supervisado.
- Visualizar los patrones ocultos en los datos a través de gráficos interactivos y estadísticos.

---

## 📂 Estructura del proyecto

| Archivo/Carpeta      | Descripción                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `main.py`            | Script principal. Orquesta todo el flujo de análisis y predicción.         |
| `limpieza.py`        | Funciones para limpiar y preparar los datos de entrada.                    |
| `graficas.py`        | Contiene múltiples funciones para crear gráficos exploratorios.            |
| `entrenamiento.py`   | Entrenamiento del modelo de machine learning.                              |
| `predictor.py`       | Carga el modelo entrenado y permite hacer predicciones.                    |
| `models/`            | Carpeta que almacena el modelo ya entrenado y serializado.                 |
| `__pycache__/`       | Cachés automáticos de Python (ignorar).                                    |

---

## 🧪 Requisitos

Este proyecto requiere Python 3.7 o superior.  
Instala los paquetes necesarios ejecutando:

```bash
pip install -r requirements.txt
