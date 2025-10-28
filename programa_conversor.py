#Este programa conversor va a leer el excel, y de ese excel leído
#agregar una Columna de PULGDAS para que puedan leerlo el usuario (los empleados de la empresa)

import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.54

# Leer el archivo excel:
df = pd.read_excel("muebles_medidas.xlsx")


# Añadir una columna al DataFrame que sea de pulgadas y se rellene con el calculo de cm / 2.54
                                    #en el'apply' le paso la función 'cm_a_pulgadas'
df["Pulgadas"] = df["Centímetros"].apply(cm_a_pulgadas)
                    #tiene tener el mismo nombre el elemento (Key) en caso "Centímetros". Sino está igual va a fallar


#Armamos un excel nuevo
df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print(
    "Conversión completada y guardada en un nuevo archivo llamado 'mueble_medidas_convertidas.xlsx'"
)