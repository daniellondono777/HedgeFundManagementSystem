import json
import requests

res = requests.get('http://127.0.0.1:8000/hfma/asset/')
print(res.json())