import pandas as pd
import numpy as np
import unicodedata


# 1️⃣ Cargar el archivo (ajusta el path si es necesario)
def cargar_csv(path):
    data = pd.read_csv(path, encoding="utf-8-sig", sep=";", index_col=False)
    # print("Datos cargados:")
    # print(data)
    return data


# 2️⃣ Normalizar nombres de columnas
def limpiar_nombres_columnas(df):
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^\w\s()]", "", regex=True)
        .str.replace(r"\s+", "_", regex=True)
    )
    return df


# 3️⃣ Limpiar caracteres especiales en el contenido
def limpiar_caracteres(df):
    def fix_str(s):
        if isinstance(s, str):
            s = unicodedata.normalize("NFKD", s)
        return s

    return df.map(fix_str)


# 4️⃣ Reemplazar respuestas como "No aplica", "Prefiero no decirlo", "..." con NaN
def reemplazar_valores_nulos(df):
    valores_nulos = ["No aplica", "Prefiero no decirlo", "...", "N/A", "n/a", "NaN"]
    return df.replace(valores_nulos, 9)


# 5️⃣ Convertir escalas de frecuencia a valores ordinales
def mapear_valores(df):
    mapeos_por_columna = {
        "género": {"Femenino": 0, "Masculino": 1, "Prefiero no decirlo": 2, "Otro": 3},
        "cuánto_tiempo_pasas_en_redes_sociales_al_día": {
            "Menos de 1 hora": 0,
            "1-3 horas": 1,
            "4-6 horas": 2,
            "Más de 6 horas": 3,
        },
        "con_qué_frecuencia_te_sientes_ansioso_después_de_usar_redes_sociales": {
            "Nunca": 0,
            "Casi nunca": 1,
            "A veces": 2,
            "Casi siempre": 3,
            "Siempre": 4,
        },
        "sientes_que_el_uso_de_redes_sociales_afecta_negativamente_tu_estado_de_ánimo": {
            "No": 0,
            "Sí": 1,
            "A veces": 3,
        },
        "has_experimentado_sentimientos_de_soledad_después_de_ver_publicaciones_de_otros": {
            "Nunca": 0,
            "A veces": 1,
            "Frecuentemente": 2,
        },
        "has_sido_diagnosticado_con_depresión_o_ansiedad": {
            "No": 0,
            "Sí": 1,
            "Prefiero no decirlo": 2,
        },
        "recibes_apoyo_psicológico_actualmente": {
            "No": 0,
            "Sí": 1,
        },
        "en_qué_momento_del_día_utilizas_más_las_redes_sociales": {
            "Madrugada": 0,
            "Mañana": 1,
            "Tarde": 2,
            "Noche": 3,
        },
        "sientes_ansiedad_o_frustración_al_ver_lo_que_otros_poseen_en_redes_sociales_y_tú_no": {
            "Nunca": 0,
            "Rara vez": 1,
            "A veces": 2,
            "Frecuentemente": 3,
            "Siempre": 4,
        },
        "crees_que_las_redes_sociales_han_afectado_tu_autoestima": {
            "No": 0,
            "Sí": 1,
            "A veces": 1,
        },
        "después_de_usar_redes_sociales_cómo_te_sientes_generalmente": {
            "Ansioso": 0,
            "Irritable": 1,
            "Más feliz": 2,
            "Mas triste": 3,
            "Sin cambios": 4,
        },
        "consideras_que_pasas_demasiado_tiempo_en_redes_sociales": {
            "No": 0,
            "Sí": 1,
            "Tal vez": 2,
        },
        "solo_si_la_respuesta_anterior_fue_si_te_gustaría_dejar_de_depender_de_las_redes_sociales": {
            "No": 0,
            "Sí": 1,
            "Tal vez": 2,
        },
    }

    for columna, mapeo in mapeos_por_columna.items():
        if columna in df.columns:
            df[columna] = df[columna].replace(mapeo)

    return df


# 6️⃣ Función principal para limpiar todo
def limpiar_datos(path_csv):
    df = cargar_csv(path_csv)
    df = limpiar_nombres_columnas(df)
    df = reemplazar_valores_nulos(df)
    df = mapear_valores(df)
    return df


def limpiar_datos_modelo(df):
    # 1️⃣ Copiar DataFrame original
    df_limpio = df.copy()

    columnas_a_conservar = [
        "cuál_es_tu_edad",
        "género",
        "país",
        "cuánto_tiempo_pasas_en_redes_sociales_al_día",
        "cuáles_redes_sociales_utilizas_con_mayor_frecuencia",
        "para_qué_utilizas_principalmente_las_redes_sociales",
        "con_qué_frecuencia_te_sientes_ansioso_después_de_usar_redes_sociales",
        "en_qué_momento_del_día_utilizas_más_las_redes_sociales",
    ]
    df_limpio = df_limpio[columnas_a_conservar]
    # print(df_limpio.to_csv(index=False))
    # 2️⃣ Renombrar columnas en la copia
    df_limpio = df_limpio.rename(
        columns={
            "cuál_es_tu_edad": "edad",
            "género": "genero",
            "país": "pais",
            "cuánto_tiempo_pasas_en_redes_sociales_al_día": "tiempo_uso",
            "cuáles_redes_sociales_utilizas_con_mayor_frecuencia": "redes_sociales",
            "para_qué_utilizas_principalmente_las_redes_sociales": "uso",
            "con_qué_frecuencia_te_sientes_ansioso_después_de_usar_redes_sociales": "ansiedad",
            "en_qué_momento_del_día_utilizas_más_las_redes_sociales": "momento_dia",
        }
    )

    # print(df_limpio.head(10))

    # 3️⃣ Transformaciones como ya tenías:
    mapa_edad = {"18-24": 1, "25-34": 2, "35-44": 3, "45-54": 4, "55+": 5}
    df_limpio["edad"] = df_limpio["edad"].map(mapa_edad)

    df_limpio["redes_sociales"] = df_limpio["redes_sociales"].str.replace("Otros: ", "")
    df_limpio["redes_sociales"] = df_limpio["redes_sociales"].str.split(",")
    df_limpio = df_limpio.explode("redes_sociales")

    print("redes_sociales:")
    print(df_limpio["redes_sociales"].unique())
    # print(df_limpio.to_csv())

    redes_unicas = {
        "Facebook": 1,
        "Instagram": 2,
        "TikTok": 3,
        "X(Twitter)": 4,
        "WhatsApp": 5,
        "Reddit": 6,
        "Discord": 7,
        "LinkedIn": 8,
        "Snapchat": 9,
        "Grindr": 10,
        "Tinder": 11,
        "Rappi y Uber eats": 12,
        "Otros": 13,
    }
    df_limpio["redes_sociales"] = df_limpio["redes_sociales"].map(redes_unicas)

    df_limpio["uso"] = df_limpio["uso"].str.replace("Otros: ", "")
    df_limpio["uso"] = df_limpio["uso"].str.split(",")
    df_limpio = df_limpio.explode("uso")

    print("uso:")
    print(df_limpio["uso"].unique())
    # print(df_limpio.to_csv())

    usos_cod = {
        "Conectar con amigos/familia": 1,
        "Entretenimiento": 2,
        "Noticias": 3,
        "Compra y venta": 4,
        "Leer narraciones": 5,
        "Aprender idiomas": 6,
        "Buscar empleo": 7,
        "Trabajo": 8,
    }
    df_limpio["uso"] = df_limpio["uso"].map(usos_cod)
    df_limpio = df_limpio.fillna(9)
    df_limpio["redes_sociales"] = df_limpio["redes_sociales"].astype(int)
    df_limpio["uso"] = df_limpio["uso"].astype(int)
    # print(df_limpio.columns.tolist())
    return df_limpio
