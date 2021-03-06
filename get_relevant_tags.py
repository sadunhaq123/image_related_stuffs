import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections
import time
#full_erroneous_list_full_two
#file1 = open('myfile.txt', 'r')
#file1 = open('full_erroneous_list_full.txt', 'r')
file1 = open('list_of_officials.txt', 'r')
Lines = file1.readlines()
list_of_names_with_most_recent_tag = []
list_of_names = []
erroneous_list = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []
first_thousand = -1
count = 0
# Strips the newline character
for line in Lines:
    first_thousand = first_thousand + 1
    if first_thousand %25 == 0:
        time.sleep(20)
    #if (first_thousand > 1000):
    #    break
    content = line.strip()
    #name_with_publisher_but_without_count = content.split(':')
    #print(name_with_publisher_but_without_count[0])
    #name_without_publisher_and_without_count = name_with_publisher_but_without_count[0].split('/')
    list_with_name_and_count = content.split(':')
    print(list_with_name_and_count[0])
    url = "https://hub.docker.com/v2/repositories/library/" + list_with_name_and_count[0] +"/tags/?page=1"
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    newDictionary = json.loads(str(soup.text))

    try:
        results = newDictionary['results']
    except KeyError:
        erroneous_list.append(url)
        print('Something happened in the results!')
        time.sleep(20)
        continue

    for j in range(len(newDictionary['results'])):
        dictionary_with_all = newDictionary['results'][j]
        name = dictionary_with_all['name']
        name_with_most_recent_tag = list_with_name_and_count[0] + ":" + name
        #print(name_with_most_recent_tag)
        list_of_names_with_most_recent_tag.insert(count, name_with_most_recent_tag)
        #print(name_with_most_recent_tag)
        break

    count = count+1



with open('full_list_of_names_with_most_recent_tag_feb_2022.txt', 'w') as file_with_list_of_names_with_most_recent_tag:
    for list_item_in_list_of_names_with_most_recent_tag in list_of_names_with_most_recent_tag:
        file_with_list_of_names_with_most_recent_tag.write('%s\n' % list_item_in_list_of_names_with_most_recent_tag)

file_with_list_of_names_with_most_recent_tag.close()


with open('full_erroneous_list_full_feb_2022.txt', 'w') as file_with_erroneous_list:
    for list_item_in_erroneous_list in erroneous_list:
        file_with_erroneous_list.write('%s\n' % list_item_in_erroneous_list)

file_with_erroneous_list.close()