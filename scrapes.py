import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections


#url = "https://hub.docker.com/api/content/v1/products/search?q=%2B&source=community" \
#      "&type=image&architecture=arm%2Carm64&type=image&page=6&page_size=25"

#url = "https://hub.docker.com/v2/search/repositories?query=%2B&is_official=False&type=image&architecture=arm%2Carm64&page=1&page_size=25"
url = "https://hub.docker.com/api/content/v1/products/search?architecture=arm,arm64&page=101&page_size=25&q=&type=image"

#url ="https://hub.docker.com/api/content/v1/products/search?%2B&source=community&architecture=arm,arm64&page=1&page_size=25&q=&type=image"
#url="https://hub.docker.com/api/content/v1/products/search?q=%2B&source=community" \
#      "&type=image&architecture=arm%2Carm64&type=image&page=1&page_size=25"
#url="https://search-api.s.us-east-1.aws.dckr.io/v2/search/repositories?is_official=false&page=2&page_size=25&query=%2B"
#url = "https://hub.docker.com/api/content/v2/products/search?%2B&source=community&architecture=arm,arm64&page=7&page_size=25&q=&type=image"
r = requests.get(url, headers={
    "Accept": "application/json"
    , "Accept-Encoding": "gzip, deflate, br"
    , "Accept-Language": "en-US,en;q=0.5"
    , "Connection": "keep-alive"
    , "Content-Type": "application/json"
    #, "Cookie": "_gcl_au=1.1.1783362476.1617501905; optimizelyEndUserId=oeu1617501905394r0.6341117205222938; _ga=GA1.2.1209652020.1617501905; ajs_anonymous_id=%221cc0d09f-e0c1-4a21-a299-d4f0423980bf%22; _mkto_trk=id:929-FJL-178&token:_mch-docker.com-1617501905488-28601; ajs_user_id=%2237e93d34a4954755a5b16d53b3c6b2a6%22; NPS_383366e9_last_seen=1618354634995; _fbp=fb.1.1618571493748.560373916; docker-id=sadunhaq123; NPS_383366e9_surveyed=true; dwf_banner=True; optimizelySegments=%7B%7D; optimizelyBuckets=%7B%7D; session_hint…ba3-02af1174230b1e-4c3f2c72-1fa400-17956c2c4a4cdb%22%2C%22%24device_id%22%3A%20%2217956c2c4a3ba3-02af1174230b1e-4c3f2c72-1fa400-17956c2c4a4cdb%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; mf_31c8bb38-cfeb-4bd8-a60c-d5650a6d6f23=|.47.1622942185247|1622942185248||0|||0|17.44|98.49041; mf_6f7d6de3-deb5-4950-9ff2-e178439823d6=|.3813240081.1618571492290$.3813240081.1618571492290|1618571492299||0|||0|17.40|56.04072; namespace=sadunhaq123; _gat=1"
    , "Host": "hub.docker.com"
    , "Referer": "https://hub.docker.com/search?q=&type=image&architecture=arm%2Carm64&page=101"
    , "Search-Version": "v3"
    , "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    , "X-CSRFToken": "3qAOPP8csAK+4frmCv6V0i3t6zAxMELJ2d1c7aS0qr0="
    , "X-DOCKER-API-CLIENT": "docker-hub/967.0.0"

})

#print(r)
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup)
#newDictionary = json.loads(r.decode("utf-8"))
newDictionary = json.loads(str(soup.text))
count_of_pages = newDictionary['count']
total_counter = 0
print(count_of_pages)
print(newDictionary)
#print("Archis: ", newDictionary['architectures'])
print("Summaries: ", newDictionary['summaries'])
dictionary_with_name_and_popularity = {}

for j in range(len(newDictionary['summaries'])):
    dictionary_with_all = newDictionary['summaries'][j]
    name = dictionary_with_all['name']
    popularity = dictionary_with_all['popularity']
    dictionary_with_name_and_popularity[name] = popularity
    # print (total_counter)
    total_counter = total_counter + 1