from bs4 import BeautifulSoup as bs
from time import sleep, perf_counter
from requests_html import AsyncHTMLSession, HTMLSession
import asyncio
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

def tj_search(query):
  baseurl = "https://www.traderjoes.com"
  url = f'{baseurl}/home/search?q={query}&section=products&global=yes'
  response = selenium_render_page(url)
  soup = bs(response, 'html.parser')
  results = soup.find_all(class_='SearchResultCard_searchResultCard__3V-_h')

  print('Trader Joe\'s')
  for item in results[:5]:
    name = item.h3.text
    price = item.find(class_='ProductPrice_productPrice__price__3-50j').text
    unit = item.find(class_='ProductPrice_productPrice__unit__2jvkA').text
    print(f'{name} --  {price} {unit}')


def albert_search(query):
  baseurl = "https://www.albertsons.com/"
  url = f'{baseurl}/shop/search-results.html?q={query}'
  response = selenium_render_page(url)
  soup = bs(response, 'html.parser')
  results = soup.find_all(class_='product-card-container')

  print('Albertson\'s')
  for item in results[:5]:
    name = item.find(class_='product-title__name').text
    pricePer = item.find(class_='product-title__qty').text
    print(f'{name} --  {pricePer}')


def selenium_render_page(url):
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  sleep(3)
  r = driver.page_source
  return r

# tj_search('bananas')
# albert_search('bananas')

    # print(url)
  # albert_search(query)
# asyncio.run(main())
query = 'chicken'
threads = []
threads.append(Thread(target=lambda: tj_search(query)))
threads.append(Thread(target=lambda: albert_search(query)))
print('running...')
for t in threads:
  t.start()

for t in threads:
  t.join()
# tj_search('chicken')
# albert_search('chicken')
print('done!')