import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Gráfico de barras: ¿Para qué utilizas principalmente las redes sociales?
def graficar_uso_redes(df):
    usos_aplanados = (
        df["para_qué_utilizas_principalmente_las_redes_sociales"]
        .str.split(",")
        .explode()
        .str.strip()
    )
    conteo = usos_aplanados.value_counts()

    plt.figure(figsize=(10, 6))
    conteo.plot(kind="bar", color="skyblue")
    plt.title("¿Para qué utilizas principalmente las redes sociales?")
    plt.xlabel("Uso Principal")
    plt.ylabel("Cantidad de personas")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


# Gráfico de barras: Frecuencia de edades de los encuestados
def graficar_edad(df):
    edades = df["cuál_es_tu_edad"].copy().value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    edades.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Frecuencia de respuestas por edad")
    plt.xlabel("Edad")
    plt.ylabel("Cantidad de personas")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


# Gráfico de pastel: Tiempo total que pasan en redes sociales al día
def grafica_pie_general(df):
    conteo = (
        df["cuánto_tiempo_pasas_en_redes_sociales_al_día"].value_counts().sort_index()
    )

    tiempo = {
        0: "Menos de 1 hora",
        1: "1-3 horas",
        2: "4-6 horas",
        3: "Más de 6 horas",
    }
    labels = [tiempo[i] for i in conteo.index]

    plt.figure(figsize=(6, 6))
    plt.pie(conteo, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Tiempo en redes sociales - General")
    plt.tight_layout()
    plt.show()


# Gráfico de dispersión: Edad vs red social más utilizada
def graficar_dispersion_edad_red(df):
    df_subset = df[
        ["cuál_es_tu_edad", "cuáles_redes_sociales_utilizas_con_mayor_frecuencia"]
    ].copy()

    df_subset["cuáles_redes_sociales_utilizas_con_mayor_frecuencia"] = df_subset[
        "cuáles_redes_sociales_utilizas_con_mayor_frecuencia"
    ].str.split(",")

    df_subset = df_subset.explode("cuáles_redes_sociales_utilizas_con_mayor_frecuencia")
    df_subset["cuáles_redes_sociales_utilizas_con_mayor_frecuencia"] = df_subset[
        "cuáles_redes_sociales_utilizas_con_mayor_frecuencia"
    ].str.strip()

    df_subset = df_subset.rename(
        columns={
            "cuáles_redes_sociales_utilizas_con_mayor_frecuencia": "red_social",
            "cuál_es_tu_edad": "edad",
        }
    )

    plt.figure(figsize=(10, 6))
    sns.stripplot(data=df_subset, x="edad", y="red_social", jitter=True, alpha=0.7)
    plt.title("Edad vs Red Social Más Utilizada")
    plt.xlabel("Edad")
    plt.ylabel("Red Social")
    plt.tight_layout()
    plt.show()


# Gráfico de pastel: Tiempo en redes sociales por género
def graficar_pie_por_genero(df):
    for genero in df["género"].dropna().unique():
        datos = df[df["género"] == genero][
            "cuánto_tiempo_pasas_en_redes_sociales_al_día"
        ].value_counts()

        generos = {
            0: "Femenino",
            1: "Masculino",
            2: "Prefiero no decirlo",
            3: "Otro",
            9: "Prefiero no decirlo",
        }

        tiempo = {
            0: "Menos de 1 hora",
            1: "1-3 horas",
            2: "4-6 horas",
            3: "Más de 6 horas",
        }

        labels = datos.index.map(tiempo)
        plt.figure(figsize=(6, 6))
        plt.pie(datos, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title(f"Tiempo en redes sociales por día - Género: {generos[genero]}")
        plt.axis("equal")
        plt.tight_layout()
        plt.show()


# Mapa geográfico: Distribución de respuestas por país
def graficar_mapa_geografico(df):
    conteo_paises = df["país"].value_counts().reset_index()
    conteo_paises.columns = ["país", "conteo"]

    fig = px.choropleth(
        conteo_paises,
        locations="país",
        locationmode="country names",
        color="conteo",
        title="Distribución geográfica de respuestas",
    )
    fig.show()


# Histograma: Respuestas por hora del día
def graficar_histograma_temporal(df):
    if "marca_temporal" not in df.columns:
        return

    df["marca_temporal"] = pd.to_datetime(df["marca_temporal"], errors="coerce")
    df = df.dropna(subset=["marca_temporal"])
    df["hora"] = df["marca_temporal"].dt.hour

    plt.figure(figsize=(10, 6))
    sns.histplot(df["hora"], bins=24, kde=False, color="coral")
    plt.title("Frecuencia de respuestas por hora del día")
    plt.xlabel("Hora del día")
    plt.ylabel("Cantidad de respuestas")
    plt.tight_layout()
    plt.show()


# Gráfico de línea: Relación entre tiempo en redes y nivel de ansiedad promedio
def graficar_scatter_plot(df):
    df_subset = df[
        [
            "cuánto_tiempo_pasas_en_redes_sociales_al_día",
            "con_qué_frecuencia_te_sientes_ansioso_después_de_usar_redes_sociales",
        ]
    ].copy()

    df_subset.rename(
        columns={
            "cuánto_tiempo_pasas_en_redes_sociales_al_día": "tiempo_uso",
            "con_qué_frecuencia_te_sientes_ansioso_después_de_usar_redes_sociales": "ansiedad",
        },
        inplace=True,
    )

    df_subset = df_subset.dropna(subset=["tiempo_uso", "ansiedad"])
    promedios = df_subset.groupby("tiempo_uso")["ansiedad"].mean()

    plt.figure(figsize=(8, 6))
    plt.plot(
        promedios.index, promedios.values, marker="o", linestyle="-", color="darkorange"
    )

    plt.title("Promedio de ansiedad según tiempo en redes sociales")
    plt.xlabel("Tiempo en redes (0=Menos de 1h ... 3=Más de 6h)")
    plt.ylabel("Ansiedad promedio (0=Nunca ... 4=Siempre)")
    plt.grid(True)
    plt.xticks([0, 1, 2, 3], ["<1h", "1-3h", "4-6h", ">6h"])
    plt.ylim(0, 4)
    plt.tight_layout()
    plt.show()


# Mapa de calor: Ansiedad según red social más utilizada
def graficar_mapa_calor(df):
    df_subset = df[
        [
            "cuáles_redes_sociales_utilizas_con_mayor_frecuencia",
            "con_qué_frecuencia_te_sientes_ansioso_después_de_usar_redes_sociales",
        ]
    ].copy()

    # 1️ Separar múltiples redes sociales por fila
    df_subset["cuáles_redes_sociales_utilizas_con_mayor_frecuencia"] = df_subset[
        "cuáles_redes_sociales_utilizas_con_mayor_frecuencia"
    ].str.split(",")
    df_subset = df_subset.explode("cuáles_redes_sociales_utilizas_con_mayor_frecuencia")
    df_subset["cuáles_redes_sociales_utilizas_con_mayor_frecuencia"] = df_subset[
        "cuáles_redes_sociales_utilizas_con_mayor_frecuencia"
    ].str.strip()

    # 2️ Eliminar nulos
    df_subset = df_subset.dropna(
        subset=[
            "cuáles_redes_sociales_utilizas_con_mayor_frecuencia",
            "con_qué_frecuencia_te_sientes_ansioso_después_de_usar_redes_sociales",
        ]
    )

    # 3️ Agrupar y calcular ansiedad promedio por red social
    df_subset = df_subset.rename(
        columns={
            "cuáles_redes_sociales_utilizas_con_mayor_frecuencia": "red_social",
            "con_qué_frecuencia_te_sientes_ansioso_después_de_usar_redes_sociales": "ansiedad",
        }
    )
    df_subset["ansiedad"] = pd.to_numeric(df_subset["ansiedad"], errors="coerce")
    ansiedad_promedio = df_subset.groupby("red_social")["ansiedad"].mean().sort_values()

    # 4️ Crear mapa de calor
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        ansiedad_promedio.to_frame().T,
        annot=True,
        cmap="Reds",
        cbar_kws={"label": "Ansiedad promedio"},
    )
    plt.title("Nivel promedio de ansiedad por red social")
    plt.yticks([], [])  # Ocultar eje y ya que solo hay una fila
    plt.tight_layout()
    print("Ansiedad promedio por red social:\n", ansiedad_promedio)
    plt.show()
