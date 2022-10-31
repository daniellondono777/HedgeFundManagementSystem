import requests
import json

data = {'name': 'TSLA', 'type': 'S', 'quantity_usd': 7700, 'issued_date': '2022-10-31', 'active_status': True, 'control_panel': 3}

res = requests.put('http://127.0.0.1:8000/hfma/asset/3/update/', json=data)
print(res.json())  