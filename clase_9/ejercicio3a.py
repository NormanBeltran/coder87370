lista_peli = []
while True:
    peli = input("Ingrese su pelicula favorita: ")
    if peli == "FIN" or peli == "fin":   
        break
    anio = input(f"Ingresa el año de estreno de {peli}: ")
    lista_peli.append(f"{peli},{anio}")
    
with open("archivo_peli.csv", "w") as archivo:
    archivo.write("Pelicula, Anio\n")
    for pelicula in lista_peli:
        archivo.write(pelicula + "\n")