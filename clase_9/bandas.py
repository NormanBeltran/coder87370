import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('bandas.csv')

# Contar bandas por año
bandas_por_año = df['año_creacion'].value_counts().sort_index()

# Crear el gráfico de barras
plt.figure(figsize=(14, 6))
barras = plt.bar(bandas_por_año.index, bandas_por_año.values, color='steelblue', edgecolor='black')

# Agregar números en cada barra
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura,
             f'{int(altura)}',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# Configurar etiquetas y título
plt.xlabel('Año de Creación', fontsize=12, fontweight='bold')
plt.ylabel('Cantidad de Bandas', fontsize=12, fontweight='bold')
plt.title('Cantidad de Bandas por Año de Creación', fontsize=14, fontweight='bold')

# Rotar etiquetas del eje X para mejor legibilidad
plt.xticks(rotation=45, ha='right')

# Agregar grid para mejor legibilidad
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Ajustar layout para evitar que se corten las etiquetas
plt.tight_layout()

# Guardar y mostrar el gráfico
plt.savefig('bandas_por_año.png', dpi=300, bbox_inches='tight')
plt.show()

print("Gráfico generado exitosamente: bandas_por_año.png")
print("\nResumen:")
print(bandas_por_año)