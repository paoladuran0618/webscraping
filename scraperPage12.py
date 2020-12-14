import requests
from bs4 import BeautifulSoup

url = 'https://www.pagina12.com.ar/'

p12 = requests.get(url) """ parseo de url """

p12.status_code """ codigo 200, si todo esta ok """

print(p12.text) """ trae el html de la pag """

p12.content
p12.headers
p12.request.headers
p12.request.method
p12.request.url """ util para redireccionamientos"""

# parseo de html

s = BeautifulSoup(p12.text, 'html.parser')
s = BeautifulSoup(p12.text, 'lxml')
type(s)
print(s)
print(s.prettify/())

secciones = s.find('ul', attrs={'class':'horizontal-list main-sections hiden-on-dropdown'}).find_all('li')
seccion = secciones[0]
links_secciones = [seccion.a.get('href') for seccion in secciones]

sec = requests.get(links_secciones[0])
sec
s_seccion = BeautifulSoup(sec.text, 'lxml')
print(s_seccion.prettify())