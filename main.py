import sys
import locale
import os

# Esta función solo te MUESTRA qué codificación usa Python
print(sys.getfilesystemencoding()) 

print(os.name)

datos_binarios = b"Hola"
print(datos_binarios)  # b'Hola'
print(type(datos_binarios))  # <class 'bytes'>

texto = "café 🔥"
print(texto.encode('utf-8'))

# ¿Qué codificación usa Python para archivos?
print(f"Filesystem encoding: {sys.getfilesystemencoding()}")

# ¿Qué codificación usa para entrada/salida estándar?
print(f"Default encoding: {sys.getdefaultencoding()}")

# ¿Qué dice tu sistema operativo sobre el locale?
print(f"Locale encoding: {locale.getencoding()}")

# Información detallada del locale
print(locale.getlocale())

# ¿En qué sistema estás?
print(f"OS name: {os.name}")

numero = 65
print(bin(numero))

letra = 'A'
numero = ord(letra)  # ord() te da el número del carácter
print(f"La letra '{letra}' es el número {numero}")

def analizar_utf8(texto):
    print(f"\n=== Analizando: '{texto}' ===")
    bytes_utf8 = texto.encode('utf-8')
    print(f"Bytes UTF-8: {bytes_utf8}")
    print(f"Bytes en hex: {bytes_utf8.hex(' ')}")
    print(f"Cantidad de bytes: {len(bytes_utf8)}")
    
    print("\nDetalle por carácter:")
    for char in texto:
        char_bytes = char.encode('utf-8')
        code_point = ord(char)
        print(f"  '{char}' (U+{code_point:04X}) -> {char_bytes} ({len(char_bytes)} byte{'s' if len(char_bytes) > 1 else ''})")

# Prueba:
analizar_utf8("Hola")
analizar_utf8("café")
analizar_utf8("中国")
analizar_utf8("🔥")

datos = b'Hola'
print(datos)  # b'Hola'  <-- Formato amigable

# Pero realmente son números:
print("Los bytes como números:")
for byte in datos:
    print(f"  {byte} = {chr(byte)} = {byte:08b}")