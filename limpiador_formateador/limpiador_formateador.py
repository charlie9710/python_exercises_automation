# Crea un script que procese un archivo de texto o string con datos "sucios" de clientes y los limpie:

# Extraiga RUTs chilenos y los valide (formato: 12.345.678-9 o 12345678-9)
# Encuentre y uniforme números de teléfono a un formato estándar (+56 9 XXXX XXXX)
# Identifique y extraiga códigos postales
# Reemplace múltiples espacios en blanco por uno solo
# Elimine caracteres especiales no deseados pero mantenga puntuación básica
import re
import os
from itertools import cycle
def limpiador_formateador():
  ruta = input("Ingresa la ruta del archivo a limpiar: ")



  if(os.path.exists(ruta) and os.path.isfile(ruta)):
    try:
      with open (ruta,'r') as archivo:
        texto = archivo.read()
        patron_rut = r"\b(\d{1,2}(?:\.?\d{3}){2}-[\dkK])\b"
        ruts = re.findall(patron_rut,texto)
        for i in ruts:
          valido = validar_rut(i)
          print(f"El rut {i} es: {valido}")
        
        patron_busqueda = r"\+?56?\s?9\s?\d{4}\s?\d{4}|\b9\s?\d{4}\s?\d{4}\b"
        texto_numeros_limpios = re.sub(patron_busqueda, estandarizar_telefono, texto)
        print(f"El texto con numeros limpios es: {texto_numeros_limpios}")
        print("----------------------------------------------------------")

        patron_codigos_postales= r"\b\d{7}\b"
        codigos_postales = re.findall(patron_codigos_postales,texto_numeros_limpios)
        for i in codigos_postales:
          print(f"Codigo postal: {i}")
        
        patron_espacios = r"\s{2,}"
        texto_espacios_limpio = re.sub(patron_espacios," ",texto_numeros_limpios)
        print(f"El texto con espacios limpios es: {texto_espacios_limpio}")
        print("----------------------------------------------------------") 
        patron_caracteres = r"[^a-zA-Z0-9\s\.,;:!?¿¡\-]"
        texto_limpio= re.sub(patron_caracteres,"",texto_espacios_limpio)
        print(f"El texto final limpio es: {texto_limpio}")


    except FileNotFoundError:
        print(f"Error: El archivo en {ruta} no existe.")
    except PermissionError:
        print("Error: No tienes permisos para leer este archivo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
  else:
    print("La ruta no es valida.")

def validar_rut(rut_completo):
    # Limpiar el RUT: quitar puntos y guion, y pasar a mayúsculas
    rut_limpio = rut_completo.replace(".", "").replace("-", "").upper()
    cuerpo = rut_limpio[:-1]
    dv_ingresado = rut_limpio[-1]
    
    # Algoritmo Módulo 11
    reverso = map(int, reversed(cuerpo))
    factores = cycle(range(2, 8))
    suma = sum(d * f for d, f in zip(reverso, factores))
    res = 11 - (suma % 11)
    
    if res == 11: dv_esperado = '0'
    elif res == 10: dv_esperado = 'K'
    else: dv_esperado = str(res)
    
    return dv_ingresado == dv_esperado

def estandarizar_telefono(match):
  numero= re.sub(r'\D',"",match.group())
  if numero.startswith("56"):
      cuerpo = numero[2:]
  else:
      cuerpo = numero
  return f"+56 9 {cuerpo[1:5]} {cuerpo[5:]}"

limpiador_formateador()