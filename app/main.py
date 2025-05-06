from limpieza import limpiar_datos

df_limpio = limpiar_datos("datos.csv")
#print(df_limpio['Marca temporal'])
#print(list(df_limpio.columns))
#print(df_limpio.head())
#print(df_limpio.to_string())
print(df_limpio.to_csv(index=False, sep=";"))