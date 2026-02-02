import requests
from bs4 import BeautifulSoup


url = "https://es.wikipedia.org/wiki/Valorant"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

try:
  response = requests.get(url, headers= headers)
  response.raise_for_status()
except requests.exceptions.RequestException as e:
  print(f"Error fetching the webpage: {e}")
else:
  soup = BeautifulSoup(response.content, 'html.parser')



links = soup.find_all('a')

for link in links:
  href = link.get('href')
  if href:
    print(f"Enlace: {href}")

headings = soup.find_all('h1')
print('----------------------------------------------------\n')
for head in headings:
  print(head.text.strip())

print('----------------------------------------------------\n')

personajes_tables = soup.find_all('table')

for tabla in personajes_tables:
    # Luego recorres cada fila dentro de ESA tabla
    for fila in tabla.find_all('tr'):
        celdas = fila.find_all(['td', 'th'])
        fila_datos = [celda.text.strip() for celda in celdas]
        
        # Validación para evitar errores de índice si la fila tiene menos de 3 celdas
        if len(fila_datos) >= 3:
            print(f"El personaje {fila_datos[0]} se describe por: {fila_datos[2]}")