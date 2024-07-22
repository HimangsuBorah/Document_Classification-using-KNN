import requests
from bs4 import BeautifulSoup


def scrape_food_text(url):
    response = requests.get(url)

    if response.status_code==200:

        soup = BeautifulSoup(response.content,'html.parser')

        article = soup.find('article',class_='single')

        if article:


            for elem_id in ['inpageEssb', 'meta2', 'newfo-Content']:
                element = article.find(id=elem_id)

                if element:
                    element.extract()
            

            for class_name in ['crossPromo', 'box']:

                elements = article.find_all(class_=class_name)

                for element in elements:
                    element.extract()

            for tag in article.find_all(True):

                if tag.name not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']:
                    tag.extract()
            

            article_text = article.get_text(separator='\n')
            title = article.find('h1').get_text().strip()

            return title,article_text
        else:
            print("Article not found in the page")
            return None
    
    else:
         print("Failed to retrieve the webpage")
         return None