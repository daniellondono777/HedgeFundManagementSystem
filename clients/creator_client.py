import requests
import json

data = {'name': 'F', 'type': 'S', 'quantity_usd': 8000, 'issued_date': '2022-11-01', 'active_status': True, 'control_panel': 3}
req = requests.post("http://127.0.0.1:8000/hfma/asset/create/", json=data)
print(req.json())