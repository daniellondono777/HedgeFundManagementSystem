import requests
import json

data = {'name': 'VW', 'type': 'S', 'quantity_usd': 15000, 'issued_date': '2022-12-31', 'active_status': True, 'control_panel': 3}
req = requests.post("http://127.0.0.1:8000/hfma/asset/create/", json=data)
print(req.json())