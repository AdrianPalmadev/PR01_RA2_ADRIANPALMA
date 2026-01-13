import pandas as pd
import numpy as np

df = pd.read_csv('ejemplo_csv.csv')

print("\n========== HEAD (primeras filas) ==========\n")
print(df.head())

print("\n========== INFO DEL DATAFRAME ==========\n")
print(df.info())

print("\n========== DESCRIBE (estadísticas básicas) ==========\n")
print(df.describe())

empleados_por_edad = df[df['edad'] > 30]
print("\n========== EMPLEADOS MAYORES DE 30 ==========\n")
print(empleados_por_edad)

empleados_por_ciudad = df[df['ciudad'] == 'Madrid']
print("\n========== EMPLEADOS DE MADRID ==========\n")
print(empleados_por_ciudad)

empleados_por_departamento = df[df['departamento'] == 'Ventas']
print("\n========== EMPLEADOS DE VENTAS ==========\n")
print(empleados_por_departamento)

df['salario_anual'] = df['salario'] * 12
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'])
df['antiguedad_anios'] = (pd.Timestamp.now() - df['fecha_ingreso']).dt.days // 365

print("\n========== DATAFRAME CON NUEVAS COLUMNAS ==========\n")
print(df)

media_salario = np.mean(df['salario'])
desviacion_salario = np.std(df['salario'])
percentiles_salario = np.percentile(df['salario'], [25, 50, 75])

print("\n========== ESTADÍSTICAS DE SALARIO ==========\n")
print(f"Media salario: {media_salario}")
print(f"Desviación estándar: {desviacion_salario}")
print(f"Percentiles 25 / 50 / 75: {percentiles_salario}")

print("\n========== MEDIA SALARIO POR CIUDAD ==========\n")
print(df.groupby('ciudad')['salario'].mean())

print("\n========== MEDIA SALARIO POR DEPARTAMENTO ==========\n")
print(df.groupby('departamento')['salario'].mean())

print("\n========== MEDIA SALARIO POR EDAD ==========\n")
print(df.groupby('edad')['salario'].mean())

antiguedad_maxima = df["antiguedad_anios"].max()
empleado_mas_antiguo = df[df["antiguedad_anios"] == antiguedad_maxima]

print("\n========== EMPLEADO MÁS ANTIGUO ==========\n")
print(empleado_mas_antiguo)

ciudad_con_mas_empleados = df['ciudad'].value_counts().idxmax()

print("\n========== CIUDAD CON MÁS EMPLEADOS ==========\n")
print(ciudad_con_mas_empleados)

departamento_mayor_salario = df.groupby('departamento')['salario'].mean().idxmax()

print("\n========== DEPARTAMENTO CON MAYOR SALARIO PROMEDIO ==========\n")
print(departamento_mayor_salario)

antiguedad_minima = df["antiguedad_anios"].min()
empleado_menos_experiencia = df[df["antiguedad_anios"] == antiguedad_minima]

print("\n========== EMPLEADO CON MENOS EXPERIENCIA ==========\n")
print(empleado_menos_experiencia)

empleados_filtrados = df[
    (df['departamento'] == 'Marketing') &
    ((df['ciudad'] == 'Barcelona') | (df['ciudad'] == 'Madrid')) &
    (df['antiguedad_anios'] > 10)
]

print(empleados_filtrados)
