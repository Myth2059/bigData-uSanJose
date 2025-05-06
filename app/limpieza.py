import pandas as pd
import numpy as np
import unicodedata

# 1️⃣ Cargar el archivo (ajusta el path si es necesario)
def cargar_csv(path):
    return pd.read_csv(path, encoding='utf-8', on_bad_lines='skip',sep=';')

# 2️⃣ Normalizar nombres de columnas
def limpiar_nombres_columnas(df):
    df.columns = (
        df.columns
       # .str.encode('latin1')  # detectamos codificación
        #.str.decode('utf-8', errors='replace')
        .str.strip()
        .str.lower()
        .str.replace(r'[^\w\s]', '', regex=True)
        .str.replace(r'\s+', '_', regex=True)
    )
    return df

# 3️⃣ Limpiar caracteres especiales en el contenido
def limpiar_caracteres(df):
    def fix_str(s):
        if isinstance(s, str):            
            s = unicodedata.normalize('NFKD', s)
        return s
    return df.map(fix_str)

# 4️⃣ Reemplazar respuestas como "No aplica", "Prefiero no decirlo", "..." con NaN
def reemplazar_valores_nulos(df):
    valores_nulos = ['No aplica', 'Prefiero no decirlo', '...', 'N/A', 'n/a', 'NaN']
    return df.replace(valores_nulos, np.nan)

# 5️⃣ Convertir escalas de frecuencia a valores ordinales
def mapear_valores(df):
    mapeos_por_columna = {
        "género":{
            "Femenino": 0,
            "Masculino": 1,
            "Prefiero no decirlo": 2,
            "Otro": 3
        },
        "cuánto_tiempo_pasas_en_redes_sociales_al_día":{
            "1-3 horas": 0,
            "4-6 horas": 1,
            "Menos de 1 hora": 2,
            "Más de 6 horas": 3
            },
        "con_qué_frecuencia_te_sientes_ansioso_después_de_usar_redes_sociales": {
            "Nunca": 0,
            "Casi nunca": 1,
            "Casi siempre": 2
        },
        "columna_2": {
            "No": 0,
            "Sí": 1,
            "Tal vez": 2
        },
        "columna_3": {
            "Casi nunca": 0,
            "A veces": 2,
            "Casi siempre": 4,
            "Siempre": 5
        }
    }

    for columna, mapeo in mapeos_por_columna.items():
        if columna in df.columns:
            df[columna] = df[columna].replace(mapeo)

    return df

# def mapear_sentimiento_generarl(df):
#     mapeo_sentimiento_general = {
#         "A veces": 0,
#         "Casi nunca": 1,
#         "Casi siempre": 2,
#         "Siempre": 3,
#         "Nunca": 4
#     }
#     columnas_objetivo = [col for col in df.columns if df[col].dtype == 'object']
#     for col in columnas_objetivo:
#         df[col] = df[col].replace(mapeo_sentimiento_general)
#     return df

# 6️⃣ Función principal para limpiar todo
def limpiar_datos(path_csv):
    df = cargar_csv(path_csv)
    df = limpiar_nombres_columnas(df)
    #df = limpiar_caracteres(df)
    df = reemplazar_valores_nulos(df)
    # df = mapear_valores(df)
    return df
