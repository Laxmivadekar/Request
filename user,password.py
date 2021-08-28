import requests

payload={'username':'Laxmi','password':'lucky@123'}

r=requests.post('https://httpbin.org/post',data=payload)
# print(r.text)#for text
print('____________________________________________')
# print(r.json()) #for json response
print('____________________________________________')
r_dict=r.json()
print(r_dict['form'])