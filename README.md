# redegal_test
Prueba para ingeniero de datos Jr de Redegal

Los ficheros de datos que se deseen emplear deben ser descargados de la siguiente pagina:

https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Para una correcta lectura de los archivos, el programa debe ser ejecutado en el mismo directorio en el que se encuentran los archivos de datos.

Cargamos pandas para mayor facilidad en el tratamiento de datos.

1. Lectura de datos: Se pide que el programa reciba como entrada cualquiera de los 4 ficheros CSV disponibles.

Para ello realizaremos un bucle de lectura que pedirá por pantalla que se inserte el nombre del archivo que se desea cargar. Es importante aqui acordarse de incluir la extensión del archivo para una correcta lectura. Ej 'fhv_tripdata_2021-01.csv'. La información será cargada en un dataframe.

De manera automática se lee el fichero lookup para incluir la información de 'borough' y 'zone'. Para la lectura de este es necesario que el usuario se encuentre en el mismo directorio que es lanzado el script, por lo que también hacemos una gestión de errores por si no fuera asi. En este caso de no encontrarse en el lugar solicitado, paramos el programa y pedimos al usuario que se cambie al directorio correspondiente, ya que de lo contrario no estaríamos empleando información crucial para el desarrollo de la tarea. 

2. Analisis: 10 destinos (incluyendo la información de Borough y Zone) con el mayor número de viajes que, individualmente, superan el percentil 0.95 en distancia por viaje.

Para ello debemos comprobar primero individualmente que viajes superan el percentil 0,95. Esta condición está sujeta a que esta columna exista ya que en el caso de querer cargar algun documento con la información de "For-Hire Vehicles" estas tablas no disponen del detalle de distancia recorrida. Actualizamos el dataframe para que cumpla esta condición.

A continuación creamos un nuevo dataframe partiendo del anteriormente mencionado, sobre el cual haremos una agrupación por el ID de localización de destino junto con el conteo de viajes que se hicieron a esta localización. Y sobre este mismo seleccionaremos aquellos resultados que tengan mayor número de viajes.

Finalmente para mostrar la información resultante, hacemos un cruze con el dataframe lookup para incluir el detalle de localización que queremos mostrar. Renombramos las columnas y las reordenamos para que presenten el mismo formato que el ejemplo mostrado.
