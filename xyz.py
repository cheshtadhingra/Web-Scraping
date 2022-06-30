import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

results =[]
results2=[]
results3=[]

driver = webdriver.Chrome(executable_path='C:/Users/Ramanujan college/Desktop/webdriver/chromedriver.exe')

driver.get('https://www.primeabgb.com/buy-online-price-india/graphic-cards-gpu/')
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll("div", attrs={'class': 'product-title-rating'}):
    name = a.find({'h3':'product-title'})
    results.append(name.text)
for b in soup.findAll("div", attrs={'class': 'product-price'}):
    price = b.find('bdi')
    results2.append(price.text)

driver.get('https://www.primeabgb.com/buy-online-price-india/graphic-cards-gpu/page/2/')
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll("div", attrs={'class': 'product-title-rating'}):
    name = a.find({'h3':'product-title'})
    results.append(name.text)
for b in soup.findAll("div", attrs={'class': 'product-price'}):
    price = b.find('bdi')
    results2.append(price.text)

driver.get('https://www.primeabgb.com/buy-online-price-india/graphic-cards-gpu/page/3/')
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll("div", attrs={'class': 'product-title-rating'}):
    name = a.find({'h3':'product-title'})
    results.append(name.text)
for b in soup.findAll("div", attrs={'class': 'product-price'}):
    price = b.find('bdi')
    results2.append(price.text)


df = pd.DataFrame({'Names': results, 'price': results2})
df.to_csv('dataset.csv', index=False, encoding='utf-8')
