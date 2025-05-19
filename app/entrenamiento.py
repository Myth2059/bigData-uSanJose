import joblib
from sklearn.ensemble import RandomForestRegressor


def entrenar_modelo(df, columnas, nombre_archivo):
    X = df[columnas]
    y = df["ansiedad"]

    modelo = RandomForestRegressor()
    modelo.fit(X, y)

    joblib.dump((modelo, columnas), f"app/models/{nombre_archivo}.pkl")


def entrenamiento_completo(df):
    # nivel de ansiedad según edad y red social
    entrenar_modelo(df, ["edad", "redes_sociales"], "edad_red_social")

    # nivel de ansiedad según edad, tiempo de consumo y red social
    entrenar_modelo(
        df, ["edad", "tiempo_uso", "redes_sociales"], "edad_tiempo_red_social"
    )

    # nivel de ansiedad según tiempo de uso, red social y para qué lo utiliza
    entrenar_modelo(df, ["tiempo_uso", "redes_sociales", "uso"], "tiempo_red_uso")

    # nivel de ansiedad según el momento del día, la red social y la edad
    entrenar_modelo(df, ["momento_dia", "redes_sociales", "edad"], "momento_red_edad")

    # nivel de ansiedad según edad, género y red social
    entrenar_modelo(df, ["edad", "genero", "redes_sociales"], "edad_genero_red_social")

    # nivel de ansiedad según edad, género, red social y tiempo de uso
    entrenar_modelo(
        df, ["edad", "genero", "redes_sociales", "tiempo_uso"], "edad_genero_red_tiempo"
    )

    # nivel de ansiedad según edad, género, red social, tiempo de uso y momento del día
    entrenar_modelo(
        df,
        ["edad", "genero", "redes_sociales", "tiempo_uso", "momento_dia"],
        "edad_genero_red_tiempo_momento",
    )

    # nivel de ansiedad según edad, género, red social y momento del día
    entrenar_modelo(
        df,
        ["edad", "genero", "redes_sociales", "momento_dia"],
        "edad_genero_red_momento",
    )
