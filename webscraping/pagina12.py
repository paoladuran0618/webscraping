import requests
from bs4 import BeautifulSoup as bs

def news_extraction(soup):
    """
    * This function receives an object of type BeautifulSoup 
    * and returns a list of dictionaries with the links to 
    * the news on that page.
    """
    news = soup.find_all('div', class_='article-item__content')
    list_news = []
    for i in news:
        dic = {'tittle':i.a.get_text(), 'link':i.a.get('href')}
        list_news.append(dic)
    return list_news

if __name__ == '__main__':
    pagina12 = requests.get('https://www.pagina12.com.ar/')
    bs_pag12 = bs(pagina12.text, 'lxml')

    #Obteniendo los links a las secciones del periodico argentino 'Pagina12'
    sections = bs_pag12.find('ul',attrs={'class':'horizontal-list main-sections hide-on-dropdown'}).find_all('li')

    print('\nSeleccione la sección de noticias que desea scrapear: \n')
    j=0
    for i in sections:
        print('* {}[{}]'.format(i.a.get_text(), j))
        j+=1
    
