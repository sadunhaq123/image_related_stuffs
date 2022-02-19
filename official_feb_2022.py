# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections


url = "https://hub.docker.com/api/content/v1/products/search?q=%2B&source=official" \
      "&type=image&architecture=arm%2Carm64&type=image&page=1&page_size=25"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
newDictionary = json.loads(str(soup.text))
count_of_pages = newDictionary['count']
total_counter = 0
print(count_of_pages)
print(newDictionary)
print("Summaries: ", newDictionary['summaries'])

print([i['popularity'] for i in newDictionary['summaries']])
print([i['name'] for i in newDictionary['summaries']])
print([str(i['popularity']) + ' ' + i['name'] for i in newDictionary['summaries']])

dictionary_with_name_and_popularity = {}

for i in range(1, count_of_pages):
    url = "https://hub.docker.com/api/content/v1/products/search?q=%2B&source=official" \
          "&type=image&architecture=arm%2Carm64&type=image&page=" + str(i) + "&page_size=25"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    newDictionary = json.loads(str(soup.text))
    try:
        page_size = newDictionary['page_size']
    except KeyError:
        print('Something happened!')
        break

    summaries =  newDictionary['summaries']
    #if (total_counter > 100):
    #    break

    if (page_size == 0):
        break
    print(newDictionary)

    for i in range(len(newDictionary['summaries'])):
        dictionary_with_all = newDictionary['summaries'][i]
        name = dictionary_with_all['name']
        popularity = dictionary_with_all['popularity']
        dictionary_with_name_and_popularity[name] = popularity
        #print (total_counter)
        total_counter = total_counter + 1
        #name = newDictionary['summaries']['name']
        #popularity = newDictionary['summaries']['popularity']
        #dictionary_with_name_and_popularity[name] = popularity

    #print([str(i['popularity']) + ' ' + i['name'] for i in newDictionary['summaries']])


print(total_counter)
#sorted_list_with_name_and_popularity=sorted((value,key) for (key,value) in dictionary_with_name_and_popularity.items())
sorted_list_with_name_and_popularity = sorted(dictionary_with_name_and_popularity.items(), key=lambda x: x[1], reverse=True)
sorted_dictionary_with_name_and_popularity = collections.OrderedDict(sorted_list_with_name_and_popularity)
#sorted_dictionary_with_name_and_popularity = sorted(dictionary_with_name_and_popularity.items(), key=lambda x: x[1])
print(sorted_dictionary_with_name_and_popularity)
with open("list_of_officials.txt", 'w') as f:
    for key, value in sorted_dictionary_with_name_and_popularity.items():
        f.write('%s:%s\n' % (key, value))

with open('list_of)officials_dict.txt', 'w') as convert_file:
    convert_file.write(json.dumps(sorted_dictionary_with_name_and_popularity))

#print(soup.prettify())
#things = soup.find_all('page_size')
#print(things)

#url = "https://hub.docker.com/api/content/v1/products/search?q=%2B&source=official&type=image&architecture=arm"
#page = urlopen(url)
#html = page.read().decode("utf-8")
#soup = BeautifulSoup(html, "html.parser")
#print(soup.get_text(","))
#print(soup.prettify())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
