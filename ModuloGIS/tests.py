import pandas as pd

# Cargar el archivo Excel en un DataFrame
df = pd.read_excel('Estructura.xlsx')

# Eliminar filas con valores nulos
df = df.dropna()

# Guardar el DataFrame limpio en un nuevo archivo Excel
df.to_excel('archivo_limpio.xlsx', index=False)
