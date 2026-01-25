# El Contador de Palabras (Básico - open y lectura)
# Crea un script que lea un archivo de texto llamado historia.txt. El programa debe:

# Abrir el archivo en modo lectura.

# Contar cuántas palabras totales tiene el texto.

# Contar cuántas veces aparece una palabra específica que el usuario introduzca por teclado.

# Mostrar ambos resultados en consola.



with open('texto.txt', 'r') as file:
  texto = file.read()
  palabras = texto.split()
  palabra = input("Introduce una palabra para verificar cuantas veces aparece en un texto: \n")
  cantidad = 0
  for i in palabras:
    if i==palabra:
      cantidad+=1
  print(f"La cantidad de palabras del texto es: {len(palabras)} y la cantidad de veces que aparece la palabra escogida es: {cantidad}")