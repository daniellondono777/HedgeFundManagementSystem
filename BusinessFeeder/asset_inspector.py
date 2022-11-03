from urllib.request import urlopen, Request
from bs4 import BeautifulSoup



class AssetInspector:
    def __init__(self, asset_ticker):
        self.asset_ticker = asset_ticker
        
    def news_getter(self):
        url = f"https://finviz.com/quote.ashx?t={self.asset_ticker}&p=d"
        request = Request(url = url, headers={'user-agent':'my-app'})
        # Respuesta de la url de FINVIZ
        response = urlopen(request)
        
        dom = BeautifulSoup(response, 'html')
        content = dom.find_all('table', {'class':'snapshot-table2', 'class':"snapshot-td2-cp"})
        
        print(content)

i1 = AssetInspector("TSLA")
i1.news_getter()