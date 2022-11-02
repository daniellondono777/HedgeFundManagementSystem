import requests
import json

data = {
        "name": "really?",
        "equity": 121412.0,
        "quarter_performance": 12.0,
        "daily_performance": 12.0,
        "managed_assets": [2,3]
    }
req = requests.post("http://127.0.0.1:8000/hfma/controlpanel/create/", json=data)
print(req.json())