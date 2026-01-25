# Procesador de Inventario (Avanzado - Módulo csv)
# Imagina que tienes un archivo llamado productos.csv con este formato: Nombre,Precio,Cantidad Manzanas,1.50,10 Pan,1.00,5

# Escribe un script que:

# Use import csv para leer el archivo.

# Calcule el valor total del inventario (Precio multiplicado por Cantidad para cada fila).

# Cree un nuevo archivo llamado resumen_inventario.txt donde escriba una sola línea diciendo: "El valor total del inventario es: [resultado]".


import csv

with open('inventario.csv', mode = 'r', newline='', encoding='utf-8') as file:
  total = 0
  inventario = csv.DictReader(file)
  for i in inventario:
    total = total + (float(i['Precio']) *float(i['Cantidad']))
  with open('resumen_inventario.txt', 'w') as f:
    f.write(f"El valor total del inventario es: {total}")
  
  print(f"El precio total de las compras es: {total}")