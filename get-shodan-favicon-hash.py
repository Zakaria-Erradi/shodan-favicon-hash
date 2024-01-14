# python 3

import mmh3
import requests
import codecs

url = input("Please Enter Url with favicon : ")
response = requests.get(url)
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print(hash)
