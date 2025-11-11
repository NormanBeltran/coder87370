"""
with open("musica.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

"""    

with open("musica.txt", "r") as archivo:
    linea = archivo.readline()
    while linea:
        print(f"--------------  {linea.strip()}")
        linea = archivo.readline()
