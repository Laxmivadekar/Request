import requests

# payload={'username':'Laxmi','password':'lucky@123'}

r=requests.get('https://httpbin.org/basic-auth/Laxmi/lucky@123',auth=('Laxmis','lucky@123'))

print(r) #unautherized responce code the responce 401 is the error authentication means the data is not found
print(r.text)
print('________________________________________________________')

r=requests.get('https://httpbin.org/basic-auth/Laxmi/lucky@123',auth=('Laxmi','lucky@123'))

print(r) #here it will gives the responce as 200
print(r.text)
print('______________________________________________________________')

# https://httpbin.org/delay/1
r=requests.get('https://httpbin.org/delay/1',timeout=3) #it will take the result for ofter the 3 seconds
print(r)

