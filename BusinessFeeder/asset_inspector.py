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
            # bs4 object
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
    
    def news_grouper(self):
        values = []
        try:
            url = f"https://finviz.com/quote.ashx?t={self.asset_ticker}&p=d"
            request = Request(url = url, headers={'user-agent':'my-app'})
            response = urlopen(request)
            dom = BeautifulSoup(response, 'html')
            content = dom.find_all('table',{'class':'fullview-news-outer'})[0]
            for i in content.find_all('td'):
                values.append(i.text)
                link = i.find('a', href=True)
                if link is not None:
                    values.append(link.get('href'))
        except:
            raise(Exception)
        news_datetime = values[::3]
        news_time = []
        news_date = []
        for i in news_datetime:
            try:
                news_time.append(i.split(' ')[1])
            except:
                news_time.append(i)

        current_time = ''
        for i in range(len(news_datetime)):
            if len(news_datetime[i].split(' ')) > 1:
                current_time = news_datetime[i].split(' ')[0]
                news_date.append(current_time)
            else:
                news_date.append(current_time)

        news_title = values[1::3]
        news_url = values[2::3]


        ret_list = dict(zip(news_title, zip(news_url,news_date,news_time)))
        return json.dumps(ret_list, indent=4)
        