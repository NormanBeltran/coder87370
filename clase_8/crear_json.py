import json

data = {}

data['cliente'] = []

data['cliente'].append({
    'nome': 'Rafael',
    'idade': 29,
    'cidade': 'São Paulo'
})

data['cliente'].append({
    'nome': 'Ana',
    'idade': 25,
    'cidade': 'Rio de Janeiro'
})

data['cliente'].append({
    'nome': 'Maria',
    'idade': 35,
    'cidade': 'Florianópolis'
})

data['cliente'].append({
    'nome': 'Jose',
    'idade': 30,
    'cidade': 'Ipanema'
})

with open('clientes.json', 'w') as archivo_json:
    json.dump(data, archivo_json, indent=4)

