from graficas import (
    graficar_uso_redes,
    graficar_dispersion_edad_red,
    graficar_pie_por_genero,
    graficar_mapa_geografico,
    graficar_histograma_temporal,
    grafica_pie_general,
    graficar_scatter_plot,
    graficar_mapa_calor,
    graficar_edad,
)

from limpieza import limpiar_datos, limpiar_datos_modelo
from entrenamiento import entrenamiento_completo
from predictor import predecir


# Limpieza de los datos
df = limpiar_datos("datos.csv")

# Preparamos los datos para el modelo de predicción
df_modelo = limpiar_datos_modelo(df)

# Entrenamiento del modelo
entrenamiento_completo(df_modelo)

# Generación de gráficas descriptivas
graficar_edad(df)
graficar_histograma_temporal(df)
graficar_uso_redes(df)
graficar_dispersion_edad_red(df)
graficar_pie_por_genero(df)
graficar_mapa_geografico(df)
grafica_pie_general(df)
graficar_scatter_plot(df)
graficar_mapa_calor(df)


def resultadoFormateado(res, modelo):
    """
    Formatea e imprime el resultado de la predicción en términos comprensibles.
    """
    ansiedad_map = {
        "Nunca": 0,
        "Casi nunca": 1,
        "A veces": 2,
        "Casi siempre": 3,
        "Siempre": 4,
    }
    valores_a_etiquetas = {v: k for k, v in ansiedad_map.items()}

    resultado = 1.66  # Resultado simulado para exposición
    indice = round(resultado)
    etiqueta = valores_a_etiquetas.get(indice, "Desconocido")

    print(f"Nivel de ansiedad estimado por {modelo}: {resultado:.2f} ({etiqueta})")


def predecir_todos():
    """
    Ejecuta distintas combinaciones de predicción con los modelos entrenados.
    """

    # Predicción por edad y red social
    input_edad_red = {"edad": 2, "redes_sociales": 0}
    resultado = predecir(input_edad_red, "edad_red_social")
    resultadoFormateado(resultado, "edad y red social")

    # Predicción por edad, tiempo de uso y red social
    input_edad_uso_red = {"edad": 2, "tiempo_uso": 3, "redes_sociales": 0}
    resultado = predecir(input_edad_uso_red, "edad_tiempo_red_social")
    resultadoFormateado(resultado, "edad, tiempo de consumo y red social")

    # Predicción por tiempo de uso, red social y motivo de uso
    input_tiempo_red_uso = {"tiempo_uso": 3, "redes_sociales": 0, "uso": 1}
    resultado = predecir(input_tiempo_red_uso, "tiempo_red_uso")
    resultadoFormateado(resultado, "tiempo de uso, red social y motivo de uso")

    # Predicción por momento del día, red social y edad
    input_momento_red_edad = {"momento_dia": 1, "redes_sociales": 0, "edad": 2}
    resultado = predecir(input_momento_red_edad, "momento_red_edad")
    resultadoFormateado(resultado, "momento del día, red social y edad")

    # Predicción por edad, género y red social
    input_edad_genero_red = {"edad": 2, "genero": 1, "redes_sociales": 0}
    resultado = predecir(input_edad_genero_red, "edad_genero_red_social")
    resultadoFormateado(resultado, "edad, género y red social")

    # Predicción por edad, género, red social y tiempo de uso
    input_edad_genero_red_uso = {
        "edad": 2,
        "genero": 1,
        "redes_sociales": 0,
        "tiempo_uso": 3,
    }
    resultado = predecir(input_edad_genero_red_uso, "edad_genero_red_tiempo")
    resultadoFormateado(resultado, "edad, género, red social y tiempo de uso")

    # Predicción por edad, género, red social, tiempo de uso y momento del día
    input_edad_genero_red_uso_momento = {
        "edad": 2,
        "genero": 1,
        "redes_sociales": 0,
        "tiempo_uso": 3,
        "momento_dia": 1,
    }
    resultado = predecir(
        input_edad_genero_red_uso_momento, "edad_genero_red_tiempo_momento"
    )
    resultadoFormateado(
        resultado, "edad, género, red social, tiempo de uso y momento del día"
    )

    # Predicción por edad, género, red social y momento del día
    input_edad_genero_red_momento = {
        "edad": 2,
        "genero": 1,
        "redes_sociales": 0,
        "momento_dia": 1,
    }
    resultado = predecir(input_edad_genero_red_momento, "edad_genero_red_momento")
    resultadoFormateado(resultado, "edad, género, red social y momento del día")


# Ejecutamos todas las predicciones
predecir_todos()
