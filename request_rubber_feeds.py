from news_feeds import get_news_feeds
from price_feeds import get_rubber_price_to_database

get_rubber_price_to_database('songkhla', 0, 2, 0, 1)
get_rubber_price_to_database('surat', 3, 4, 2, 3)
get_rubber_price_to_database('nakorn', 5, 6, 4, 5)
get_rubber_price_to_database('yala', 7, 8, 6, 7)
get_rubber_price_to_database('buriram', 9, 10, 8, 9)
get_news_feeds(5)
