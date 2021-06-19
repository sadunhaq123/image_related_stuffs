import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections



file1 = open('random_word_list.txt', 'r')
Lines = file1.readlines()
list_of_names = []
list_with_hits = []
list_with_errors = []
line_number = 0
count = 0
successful_hits = 0
# Strips the newline character
for line in Lines:
    count_of_pages = 1
    content = line.strip()
    user = content
    print(content)
    count = count + 1
    #url = "https://hub.docker.com/u/" + content
    url = "https://hub.docker.com/v2/repositories/" + content +"/"
    #url = "https://hub.docker.com/v2/repositories/" + "prom" + "/"
    r = requests.get(url)
    #print (url +" " + str(r.status_code))
    soup = BeautifulSoup(r.content, 'html.parser')
    newDictionary = json.loads(str(soup.text))
    #jsonify = r.json()
    try:
        get_count = newDictionary['count']
    except KeyError:
        list_with_errors.append(content)
        continue

    #print(get_count)
    if get_count > 0:
        successful_hits = successful_hits + 1
        print ("OK")
        list_with_hits.append(content)
    #if count > 100:
    #    break

print(successful_hits)
print("-------------")
print(list_with_hits)
print("-------------")
print(list_with_errors)