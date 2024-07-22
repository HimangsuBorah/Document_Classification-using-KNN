import json
import os

from dotenv import load_dotenv
from database import Database
from preprocessor import text_preprocessing


def read_json_file(file_path):
    with open(file_path,'r') as file:
        data=json.load(file)
        return data


load_dotenv()
db_url=os.getenv('MONGO_URL')

db = Database('Document-Classification-DB','Articles',db_url)

articles = read_json_file('/home/himangsu/Code/Python/notebookenv/ML_Models/document_knn/sports_article.json')

for article in articles:
    article_text=article['Article']
    category=article['Category']
    title=""

    if article_text:

        preprocessed_text = text_preprocessing(article_text)



        data = {
            "url":"",
            "category":category,
            "title":title,
            "text":article_text,
            "preprocessed_text": preprocessed_text,
            "len-raw-text":len(article_text.split()),
            "len-preprocessed-text":len(preprocessed_text.split())
        }

        db.insert_data(data)


