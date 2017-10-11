from pprint import pprint
import datetime
import requests
import sqlalchemy
from bs4 import BeautifulSoup
from sqlalchemy import text
from tqdm import tqdm

import db

engine = sqlalchemy.create_engine(db.DB.web_db())


def get_news_feeds(page_count):
    limit_start = 0
    for i in range(0, page_count):

        url = "http://www.rubberthai.com/index.php/newsyang"

        querystring = {"limitstart": limit_start}

        headers = {
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        soup = BeautifulSoup(response.text, "html.parser")
        news_list = soup.findAll("div", {"class": "catItemBody"})
        for j in tqdm(news_list):
            title = j.find("h3", {"class", "catItemTitle"}).text.strip().replace(" ", "").replace("@", "")[:-12]
            my_date = j.find("span", {"class", "catItemDateCreated"}).text.strip()
            data_date = datetime.datetime.strptime(my_date, '%d %b %Y').strftime('%Y-%m-%d')
            views = j.find("div", {"class", "catItemHitsBlock"}).text.strip()[:-6]
            content = j.find("div", {"class", "catItemIntroText"}).text.strip()
            news_feed = {
                'data_date': data_date,
                'title': title,
                'content': content,
                'views': views,
            }
            engine.execute(text("""
                                        REPLACE INTO rubber_news
                                          (data_date,title,content, views)
                                        VALUES
                                         (:data_date,:title,:content, :views)
                                    """), news_feed)
        limit_start += 15



