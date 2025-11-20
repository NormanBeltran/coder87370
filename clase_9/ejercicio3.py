# Nombre del archivo donde se guardará la colección
nombre_archivo = 'peliculas.csv'
print(f"--- Tu Colección de Películas ---")
print(f"Los datos se guardarán en el archivo '{nombre_archivo}'.")
print("Introduce 'FIN' en el nombre de la película para terminar.")
while True:
# Solicitar el nombre de la película al usuario
    pelicula = input("\nNombre de la película: ")
# Condición de salida del bucle
    if pelicula.upper() == 'FIN':
        print("\nFinalizando la captura. ¡Tu colección ha sido guardada!")
        break
    # Solicitar el año de estreno
    anio = input(f"Año de estreno de '{pelicula}': ")
    
    # Abrir el archivo en modo 'append' (añadir) para no sobrescribir los datos
    with open(nombre_archivo, 'a') as archivo:
        # Escribir la película y el año en formato CSV (valor1,valor2)
        archivo.write(f"{pelicula},{anio}\n")
    print(f"¡'{pelicula}' se ha añadido a tu colección!")