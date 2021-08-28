import requests
r=requests.get('https://imgs.xkcd.com/comics/python.png')
# print(r.content)   #it gives the bytes of image in the formate of code

# with open('comic.png','wb') as f:
#     f.write(r.content)
