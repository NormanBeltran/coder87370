import sys

if len(sys.argv) != 3:
    print("Error, debe ingresar 2 argumentos uno es la base y el otro la altura")
    sys.exit(1)
    
base = sys.argv[1]
altura = sys.argv[2]

for i in range(int(altura)):
    print("." * int(base))
    