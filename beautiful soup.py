from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup=BeautifulSoup(html_file,'lxml')

# print(soup)       #so, it will gives the o/p as it is the html code
# print(soup.prettify())   #it will be gives the html code as an indent
# print('________________________________________________________________')

# match=soup.title
# print(match)  #it will produces the o/p as with title tag and name

# print('________________________________________________________________')

# match=soup.title.text
# print(match)  #ifor i in image:
    j=i.img['src']
    list.append(j)#it only gives the output as only title name

print('________________________________________________________________')

match=soup.div.find('div',class_='footer')   #a class of folder 
print(match) #in html code we didnt used at paragraphs 

