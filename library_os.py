import os

#Obtener el directorio actual
cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)

#Listar los archivos .csv
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
print("Los archivos csv son", csv_files)

#renombrar un archivo
os.rename('ventas_mensuales.csv', 'archivo_renombrado.csv')
print("Archivo renombrado")

#Listar los archivos .csv
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
print("Los archivos csv son", csv_files)