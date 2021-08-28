from bs4 import BeautifulSoup
import requests

source=requests.get('http://coreyms.com').text

soup=BeautifulSoup(source,'lxml')

article=soup.find('article')
print(article.prettify())

# summary=article.find('div',class_='entry-content').p.text
# print(summary)
# print(soup.prettify()) #it gives total code in indent

# print(soup)  #it give total brief code

# article=soup.find('article')
# print(article.prettify())

# headline= article.h2.a.text
# print(headline)