import sys
import pandas as pd

# 1. Lectura de datos.

df = pd.DataFrame([]) # definimos un dataframe vacío para actualizarlo posteriormente con la información del archivo que queremos cargar.

while df.empty: # Esta condición lógica devuelve True si el dataframe es vacío, por lo que el bucle se parará cuando se cargue información.
    print('Introduce el nombre del archivo que quieres usar:')
    filename = input()
    print(filename)
    try:    #usamos la estrategia de try/except para gestionar nombres de archivo no correctos.
        df = pd.read_csv(filename, dtype = {'store_and_fwd_flag': str}) #especificamos el tipo de dato, ya que estaba dando error de lectura debido a los tipos de dato
    except FileNotFoundError:
        print('El nombre de archivo no es correcto, prueba otra vez') 
    
try: # gestionamos si el usuario se encuentra en el directorio correcto.
    df_lookup = pd.read_csv('taxi+_zone_lookup.csv') #cargamos el archivo lookup para cruzarlo posteriormente.
except FileNotFoundError:
    print('El directorio de ejecución debe ser el mismo que donde se encuentran los archivos, cambie el directorio y relance')
    sys.exit(1)
    
# 2. Analisis

if 'trip_distance' in df.columns:   # algunos archivos no disponen de esta información, en ese caso nos saltamos este paso.
    df = df[df.trip_distance  > df.trip_distance.quantile(0.95)] # actualizamos el dataframe aplicando el filtrado del percentil 0.95 


df_grouped = df.groupby(['DOLocationID']).size().reset_index(name='trips') # creamos un subdataframe que agrupe los id de destino de localziacion y los conteos a cada destino. Estos ultimos en la columna 'trips'
df_grouped = df_grouped.nlargest(10, 'trips').reset_index() # cogemos los 10 valores mas altos de numero de viajes y reseteamos el indice para que el conteo de indice empiece desde el 0 y no quede el valor previo de cada columna anterior a quedarnos con los valores mas altos.

results = pd.merge(df_grouped,df_lookup, left_on='DOLocationID', right_on='LocationID') # hacemos un cruce entre las dos tablas. El cruce se realiza de tal modo que solo coge la intersección de los valores que coinciden en las dos tablas.
results = results[['trips','Borough', 'Zone']] # reordenamos los resultados y posteriormente les cambiamos el nombre a las columnas.
results.rename(columns={'Borough':'end_borough', 'Zone': 'end_zone'}, inplace=True) # indicamos inplace = True para que los cambios se sobreescriban sobre el propio dataframe, evitando asi que se cree una copia del mismo.
print(results)