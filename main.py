# Парсим согластно fl заказу: https://www.fl.ru/projects/4801912/parsing-kataloga.html
# Выбранна странчка для парсинга https://www.game29.ru/products?page=1&category=926
# План
# 1. Получить html страничку                            OK
# 2. Получить кол-во страниц                            OK
# 3. Генерировать адреса страничек                      OK
# 4. Получить данные с странички 1(название, цена)
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.game29.ru/products?page=1&category=926'
base_url = 'https://www.game29.ru/products?'
page_part = 'page='
query_part = '&category=926'

headers = {
    "Accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# .find_all('a')[-2].get('href')
def name_consol(html):
    soup = BeautifulSoup(html, 'lxml')
    name = soup.findAll('div', class_='col-lg-5 col-md-5 col-sm-5 col-xs-5 cart-item-name')
    # for names in name:
    #     print(names.text.strip())

    price = soup.find_all('div', class_='col-lg-2 col-md-2 col-sm-2 col-xs-2 cart-item-price')

    for prices in price:
        print(prices.text.strip())
    # print(price)


def get_total_page(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('ul', class_='pagination-new').find_all('a')[-2].get('href')
    total_pages = pages.split('=')[-1]
    # print(total_pages)
    return total_pages


def get_html(url):
    r = requests.get(url, headers=headers)
    # print(r.text)
    return r.text


def main():
    pages = get_total_page(get_html(url))
    # print(pages)
    print(name_consol(get_html(url)))
    # for i in range(int(pages) + 1):
    #     print(base_url + page_part + str(i) + query_part)


if __name__ == '__main__':
    main()
