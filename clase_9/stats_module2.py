def calcular_promedio (datos):
    suma=sum (datos)
    cantidad= len(datos)
    promedio= suma/cantidad
    return promedio

def encontrar_maximo(datos):
  """Encuentra el valor máximo en una lista de números."""
  return max(datos)
def encontrar_minimo(datos):
  """Encuentra el valor máximo en una lista de números."""
  return min(datos)

def saludar_analista():
    return "Análisis iniciado. Bienvenido al Módulo de Estadísticas."