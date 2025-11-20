import stats_module2 as sm

datos_prueba = [10, 25, 5, 42, 18, 33]
saludo = sm.saludar_analista()
print(saludo)

print(f"Datos: {datos_prueba}")
print(f"El promedio de los datos es: {sm.calcular_promedio(datos_prueba)}")
print(f"El maximo de los datos es: {sm.encontrar_maximo(datos_prueba)}")
print(f"El minimo de los datos es: {sm.encontrar_minimo(datos_prueba)}")