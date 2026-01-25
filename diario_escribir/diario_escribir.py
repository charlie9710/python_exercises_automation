# El Diario de Notas (Intermedio - open y escritura)
# Crea una aplicación sencilla de "Diario" que permita al usuario añadir entradas. El programa debe:

# Preguntar al usuario: "¿Qué quieres escribir en tu diario hoy?".

# Abrir (o crear si no existe) un archivo llamado diario.txt.

# Escribir la frase del usuario al final del archivo, sin borrar lo que ya existía, y añadiendo un salto de línea al final.

# Al terminar, el programa debe imprimir todo el contenido actual del diario para que el usuario vea su historial.

with open('diario.txt', 'a') as diario:
  escritura = input("Que quieres escribir el dia de hoy?: ")
  diario.write(f"{escritura}\n")


with open('diario.txt', 'r') as texto:
    texto_final = texto.read()
    print(f"El texto final es: \n {texto_final}")