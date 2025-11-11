import json

with open('clientes.json', 'r') as f:
    data = json.load(f)
    for cliente in data['cliente']:
        print(cliente['nome'], cliente['idade'], cliente['cidade'])