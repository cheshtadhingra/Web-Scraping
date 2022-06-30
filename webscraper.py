import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Ramanujan college/Desktop/webdriver/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findAll(attrs='css-6kffxp eb77b220'):
    name  = element.find('h4')
    if name not in results:
        results.append(name.text)
print(results)


