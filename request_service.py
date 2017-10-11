from pprint import pprint

import requests
from bs4 import BeautifulSoup

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; " \
          "name=\"start\"\r\n\r\n2017-01-01\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: " \
          "form-data; name=\"end\"\r\n\r\n2017-12-31\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW-- "

headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "e2509e58-9370-0af0-6fe6-ae80b61da66a"
}


def get_rss_price():
    url = "http://www.rubberthai.com/yang/HisRSS.php"

    response = requests.request("POST", url, data=payload, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    all_list = soup.findAll("tr")
    return all_list


def get_uss_price():
    url = "http://www.rubberthai.com/yang/HisUSS.php"
    response = requests.request("POST", url, data=payload, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    all_list = soup.findAll("tr")
    return all_list


def get_local_price():
    url = "http://www.rubberthai.com/yang/HisLoc.php"
    response = requests.request("POST", url, data=payload, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    all_list = soup.findAll("tr")
    return all_list


def get_future_price():
    url = "http://www.rubberthai.com/yang/HisPreorder.php"
    response = requests.request("POST", url, data=payload, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    all_list = soup.findAll("tr")
    return all_list
