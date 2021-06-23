import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections
from json import JSONDecodeError
import time



file1 = open('community_list_from_zerouali.txt', 'r')
Lines = file1.readlines()
#Lines = ['yacy', 'zuz9', 'ara98']

list_of_names = []
list_of_errors = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []
counting_dictionary = dict()
dictionary_with_name_and_arm_image = {}
list_of_arm_image_names = []
line_number = 1
count = 0
# Strips the newline character
for line in Lines:
    count_of_pages = 1
    content = line.strip()
    user = content.split('/')
    content = user[0]
    print(content)
    #url = "https://hub.docker.com/u/" + content
    url = "https://hub.docker.com/v2/repositories/" + content +"/?page_size=25&page=" + str(count_of_pages) + "&ordering=last_updated"
    #url = "https://hub.docker.com/v2/repositories/" + content + "/?page_size=25&page=" + str(count_of_pages) + "&ordering=last_updated"


    r = requests.get(url)


    try:
        soup = BeautifulSoup(r.content, 'html.parser')
        newDictionary = json.loads(str(soup.text))
        print(soup.text)
        print(url)
        next_url = newDictionary['next']
        print(next_url)
    except Exception as e:
        print("Do Something in lines")
        list_of_errors.append(content)
        print(e)
        time.sleep(20)
        continue
        #r = requests.get(url)
        #soup = BeautifulSoup(r.content, 'html.parser')
        #newDictionary = json.loads(str(soup.text))
        #next_url = newDictionary['next']



    while next_url is not None:

        print("Have next URL")
        url = "https://hub.docker.com/v2/repositories/" + content + "/?page_size=25&page=" + str(count_of_pages) + "&ordering=last_updated"

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        try:
            newDictionary = json.loads(str(soup.text))
            print("In next_url")
            print(soup.text)
            next_url = newDictionary['next']
        except Exception as e:
            print("Do Something in next_url")
            print(e)
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            newDictionary = json.loads(str(soup.text))
            next_url = newDictionary['next']



        #print(newDictionary)
        for j in range(len(newDictionary['results'])):
            dictionary_with_all = newDictionary['results'][j]
            name = dictionary_with_all['name']
            if "arm" in name:
                count = count + 1
                print(name)
                user_with_arm_name = user + ":" + name
                list_of_arm_image_names.append(user_with_arm_name)
        count_of_pages = count_of_pages + 1

    #break
    if (next_url is None):
        print("No next URL")
        for j in range(len(newDictionary['results'])):
            dictionary_with_all = newDictionary['results'][j]
            name = dictionary_with_all['name']
            if "arm" in name:
                count = count + 1
                print(name)
                user_with_arm_name = user + ":" + name
                list_of_arm_image_names.append(user_with_arm_name)

    print(list_of_arm_image_names)
    print(count)
    line_number = line_number + 1

print("PRINTING")
print(count)

with open('list_of_arm_images_fullfrom_zerouali.txt', 'w+') as f1:
    # write elements of list
    for items in list_of_arm_image_names:
        f1.write('%s\n' % items)

    print("File for arm images written successfully")

# close the file
f1.close()

print(list_of_errors)
