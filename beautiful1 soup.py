from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup=BeautifulSoup(html_file,'lxml')

for article in soup.find_all('div',class_='article'):

    headline= article.h2.a.text

    summury=article.p.text
    print(summury)  #itgives blank because there is in html file articles are not there
print()

