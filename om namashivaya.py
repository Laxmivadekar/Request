import requests
r=requests.get('https://xkcd.com/353/')
print(r)    #it gives response
print('__________________________________')
print(dir(r))   #it will gives attributes and methods
print('______________________________________')
# print(help(r))  #it will give brief imformation
print('______________________________________')
# print(r.text)    #it will gives httml code


