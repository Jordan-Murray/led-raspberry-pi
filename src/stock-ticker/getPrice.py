from urllib3.util.retry import Retry
import requests
from requests.adapters import HTTPAdapter

def retry_session(retries, session=None, backoff_factor=0.3):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        method_whitelist=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def getprice(coinId,fiatId):
    endpoint = "https://api.coingecko.com/api/v3/simple/price?ids="+ coinId + "&vs_currencies=" + fiatId + "&include_24hr_change=true"
    session = retry_session(retries=1)
    response = session.get(url=endpoint)
    json_obj = response.json()
    return {
        'price': json_obj[coinId][fiatId],
        'change_24h': json_obj[coinId][fiatId + '_24h_change']
    }
