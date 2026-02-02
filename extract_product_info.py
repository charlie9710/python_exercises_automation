from bs4 import BeautifulSoup


html_content = """<div class="product">
  <h1>Awesome Headphones</h1>
  <p class="price">$99.99</p>
  <p class="description">These headphones offer amazing sound quality!</p>
</div>"""


soup = BeautifulSoup(html_content, 'html.parser')

name = soup.find('h1')

price = soup.find('p', class_='price')

description = soup.find('p', class_='description')

print(f"El nombre es: {name.get_text()}")
print(f"El precio es: {price.get_text()}")
print(f"La descripcion es: {description.get_text()}")