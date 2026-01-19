def explorar_bytes ():
  while True:
    print('-'*60)

    texto = input("Ingresa tu texto: ")

    if(texto == 'salir'):
      break

    for i, char in enumerate(texto):
      code_point = ord(char)
      print(f"\n El {char} tiene representacion en utf-8 de: {char.encode('utf-8')} y la cantidad de bytes son {len(char.encode('utf-8'))} ")
      print (f"En binario es : {' '.join(f'{b:08b}' for b in char.encode('utf-8'))}")

    print('-'*60)


explorar_bytes()

# texto= "hola mundo"
# bytes_utf8 = texto.encode('utf-8')
# print(f"Bytes UTF-8: {bytes_utf8}")

# print(f"La lista de bytes son: {list(bytes_utf8)}")

# for i in texto:
#   numero = ord(i)
#   print(f"En binario el caracter {i} es: {numero:08b}")

numero= 36

print(f"El numero: {numero} es {'par' if numero%2==0 else 'impar'}")