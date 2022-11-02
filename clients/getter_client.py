import json
import requests

res = requests.get('http://127.0.0.1:8000/hfma/employee/3')
data = res.json()
for i in data:
    print(i, data.get(i))

for i in data['managed_assets']:
    req = requests.get('http://127.0.0.1:8000/hfma/asset/{}'.format(i))
    print('asset: {}'.format(req.json()['name']))