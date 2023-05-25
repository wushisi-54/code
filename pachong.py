import requests

res = requests.get('http://www.douban.com') 
print(res) 
print(type(res))
