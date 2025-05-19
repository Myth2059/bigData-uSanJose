import joblib
import pandas as pd
import os


def cargar_modelos():
    modelos = {}
    for archivo in os.listdir("app/models"):
        if archivo.endswith(".pkl"):
            nombre = archivo.replace(".pkl", "")
            modelo, columnas = joblib.load(f"app/models/{archivo}")
            modelos[nombre] = (modelo, columnas)  #  usar string como clave
    return modelos


MODELOS = cargar_modelos()


def predecir(json_input, nombre_modelo):
    df_input = pd.DataFrame([json_input])

    if nombre_modelo not in MODELOS:
        raise ValueError(f"No existe un modelo llamado '{nombre_modelo}'")

    modelo, columnas = MODELOS[nombre_modelo]
    X = df_input[list(columnas)]
    return modelo.predict(X)[0]
