# Desarrolla un programa que lea un texto y extraiga toda la información relevante usando regex:
# Todos los números de teléfono (formato: +56 9 1234 5678 o similar)
# Todas las fechas (formatos: DD/MM/YYYY, DD-MM-YYYY, YYYY-MM-DD)
# Todas las URLs (http://, https://, www.)
# El programa debe mostrar un reporte organizado con cada tipo de información encontrada.

import re
import os

def extractor():
  ruta = input("Ingresa la ruta del archivo a leer: ")
  if (os.path.exists(ruta) and os.path.isfile):
    try:
        with open(ruta, "r") as archivo:
            texto= archivo.read()
            patron_numero = r"\+56\s?9\s[0-9]{4}\s[0-9]{4}"
            patron_fecha = r"[0-9]{2}[/-][0-9]{2}[/-][0-9]{4}|[0-9]{4}[/-][0-9]{2}[/-][0-9]{2}"
            patron_url = r"https?://[A-Za-z0-9._%+-]+\.[a-z]{2,}|www\.[A-Za-z0-9._%+-]+\.[a-z]{2,}"

            numeros = re.findall(patron_numero,texto)
            fechas = re.findall(patron_fecha,texto)
            urls = re.findall(patron_url,texto)

            print(f"La cantidad de numeros de telefono son: {len(numeros)}")
            print(f"La cantidad de fechas son: {len(fechas)}")
            print(f"La cantidad de urls son: {len(urls)}")
    except FileNotFoundError:
        print(f"Error: El archivo en {ruta} no existe.")
    except PermissionError:
        print("Error: No tienes permisos para leer este archivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
  else:
     print("La ruta proporcionada no es valida.")

extractor()