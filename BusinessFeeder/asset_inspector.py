from operator import indexOf
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

class AssetInspector:
    def __init__(self, asset_ticker):
        self.asset_ticker = asset_ticker
        
    def financial_indicator_getter(self):
        try:
            url = f"https://finviz.com/quote.ashx?t={self.asset_ticker}&p=d"
            request = Request(url = url, headers={'user-agent':'my-app'})
            # Respuesta de la url de FINVIZ
            response = urlopen(request)
            
            dom = BeautifulSoup(response, 'html')
            content = dom.find_all('table', {'class':'snapshot-table2'})[0] # <class 'bs4.element.Tag'>
            values = []
            for i in content.find_all('td'):
                values.append(i.text)
            concept = values[::2]
            isf = values[1::2]
            json_return = json.dumps(dict(zip(concept, isf)), indent=4)
            return json_return
        except:
            raise(Exception)
