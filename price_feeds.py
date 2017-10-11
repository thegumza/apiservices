from pprint import pprint

from tqdm import tqdm

import db

import request_service
import sqlalchemy
from sqlalchemy import text

month = []
month_list = ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน',
              'พฤษภาคม', 'มิถุนายน', 'กรกฏาคม', 'สิงหาคม',
              'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']
year = ''
day = ''
index = -1

engine = sqlalchemy.create_engine(db.DB.web_db())

local_all_list = request_service.get_local_price()
rss_all_list = request_service.get_rss_price()
uss_all_list = request_service.get_uss_price()


def insert_to_database(province_name, price_feed):

    engine.execute(text("""
                            REPLACE INTO {}
                              (data_date,local_price,latex_price, rss_price, rss_volume,uss_price, uss_volume) 
                            VALUES 
                             (:data_date,:local_price,:latex_price, :rss_price, :rss_volume,:uss_price, :uss_volume) 
                        """.format(province_name)), price_feed)


def get_rubber_price_to_database(province_name, local_index, latex_index, price_index, volume_index):
    month_index = -1
    global year, day
    for i, j, k in zip(tqdm(local_all_list), rss_all_list, uss_all_list):
        local_list = i.findAll("td")
        if len(i.findAll("td", {"class", "year"})) > 0:
            year = str(int(i.find("td", {"class", "year"}).text.strip()) - 543)
        if len(local_list) == 15:
            if len(i.findAll("td", {"class", "month"})) > 0:
                month.append(i.find("td", {"class", "month"}).text.strip())
                month_index += 1
            if len(i.findAll("td", {"class", "day"})) > 0:
                day = i.find("td", {"class", "day"}).text.strip().zfill(2)
                month_name = str(month_list.index(month[month_index]) + 1).zfill(2)
                date = year + '-' + month_name + '-' + day
                all_local_price = i.findAll("td", {"class", "num2"})
                all_rss_price = j.findAll("td", {"class", "num2"})
                all_uss_price = k.findAll("td", {"class", "num2"})
                local_price = all_local_price[local_index].text.strip()
                latex_price = all_local_price[latex_index].text.strip()
                rss_price = all_rss_price[price_index].text.strip()
                rss_volume = all_rss_price[volume_index].text.strip().replace(",", "")
                uss_price = all_uss_price[price_index].text.strip()
                uss_volume = all_uss_price[volume_index].text.strip().replace(",", "")
                price_feed = {
                    'data_date': date,
                    'local_price': local_price,
                    'latex_price': latex_price,
                    'rss_price': rss_price,
                    'rss_volume': rss_volume,
                    'uss_price': uss_price,
                    'uss_volume': uss_volume,
                }
                insert_to_database(province_name, price_feed)
