import requests
import random
from bs4 import BeautifulSoup as bs
proxies = []

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    global proxies
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            #print(host)
            proxies.append(host)
        except IndexError:
            continue
    return proxies



def get_session(proxies):
    get_free_proxies()
    #global proxies
    # construct an HTTP session
    session = requests.Session()
    # choose one random proxy
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session

get_session(proxies)


for i in range(len(proxies)):
    s = get_session(proxies)
    print("HH")
    try:
        print("Request page with IP:", s.get("http://icanhazip.com", timeout=1.5))
    except Exception as e:
        continue