import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections

def findNthOccur(string, ch, N):
    occur = 0;

    # Loop to find the Nth
    # occurence of the character
    for i in range(len(string)):
        if (string[i] == ch):
            occur += 1

        if (occur == N):
            return i

    return -1


file1 = open('erroneous_list_two.txt', 'r')
Lines = file1.readlines()
list_of_names_with_most_recent_tag = []
list_of_names = []
erroneous_list = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []

count = 0
ch = '/'
# Strips the newline character
for line in Lines:

    content = line.strip()
    url = content
    print(url)
    #print(name_with_publisher_but_without_count[0])
    #name_without_publisher_and_without_count = name_with_publisher_but_without_count[0].split('/')
    #url = "https://hub.docker.com/v2/repositories/" + name_with_publisher_but_without_count[0] +"/tags/?page=1"
    #print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    newDictionary = json.loads(str(soup.text))

    try:
        results = newDictionary['results']
    except KeyError:
        erroneous_list.append(url)
        print('Something happened in the results!')
        continue

    for j in range(len(newDictionary['results'])):
        dictionary_with_all = newDictionary['results'][j]
        name = dictionary_with_all['name']
        name_with_most_recent_tag = url[findNthOccur(url, ch, 5) + 1: findNthOccur(url, ch, 7)] + ":" + name
        list_of_names_with_most_recent_tag.insert(count, name_with_most_recent_tag)
        #print(name_with_most_recent_tag)
        break

    count = count+1

with open('list_of_names_with_most_recent_tag_three.txt', 'w') as file_with_list_of_names_with_most_recent_tag_two:
    for list_item_in_list_of_names_with_most_recent_tag in list_of_names_with_most_recent_tag:
        file_with_list_of_names_with_most_recent_tag_two.write('%s\n' % list_item_in_list_of_names_with_most_recent_tag)

file_with_list_of_names_with_most_recent_tag_two.close()


with open('erroneous_list_three.txt', 'w') as file_with_erroneous_list_two:
    for list_item_in_erroneous_list in erroneous_list:
        file_with_erroneous_list_two.write('%s\n' % list_item_in_erroneous_list)

file_with_erroneous_list_two.close()