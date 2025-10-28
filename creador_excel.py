import pandas as pd

# Dataframe es la información básica con el nombre de las piezas y centimetros para poder armar el Excel

        #este diccionario los key-values tienen que coincider en número porque esto tiene que coincidir
        #con las columnas del excel: PIEZAS - CENTIMETROS
data = {
    "Piezas:": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centímetros": [40, 120, 60, 30, 180],  
}

#para poder crear el dataframe

#usamos esta variable
df =  pd.DataFrame(data) #y utilizo pandas (pd.) para crear el dataframe

# Guardar el DataFrame en un archivo Excel
df.to_excel("muebles_medidas.xlsx", index=False)