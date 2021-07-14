import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections
import time
import random

file1 = open('fixed_repos_list.txt', 'r')
proxies_list = []

#Lines = ['kubernetesui/dashboard']
Lines = file1.readlines()
list_of_names = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []
list_with_errors =[]
list_of_names_with_arm = []


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    #soup = bs(requests.get(url).content, "html.parser")
    global proxies_list
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            #print(host)
            proxies_list.append(host)
        except IndexError:
            continue
    return proxies_list


count=0
count_of_arm = 0
line_number=1
file_tracker_number=1
#get_free_proxies()
# Strips the newline character
for line in Lines:
    count = count + 1
    if count % 25 == 0:
        time.sleep(10)
    bool_arm_not_found = True
    content = line.strip()
    print(content)
    #break
    list_of_names.append(content)
    #url = "https://hub.docker.com/v2/repositories/kubernetesui/dashboard/tags/?page=1"
    url = "https://hub.docker.com/v2/repositories/" + content + "/tags/?page=1"
    try:
        #get_free_proxies()
        #random_proxy = (random.choice(proxies_list))
        #print(random_proxy)
        #proxy = {"http": random_proxy, "https": random_proxy}
        #r = requests.get(url, proxies=proxy)
        r = requests.get(url)
    except Exception as ex:
        list_with_errors.append(content)
        print("Hitting with errors ", content)
        print("Errors", count)
        print(ex)
        continue
    #r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        newDictionary = json.loads(str(soup.text))
        #print(soup.text)
        get_count = newDictionary['count']
        results = newDictionary['results']
        #print(results[0])
        #print("Succesful Hits", content)
    except Exception as e:
        list_with_errors.append(content)
        print("Hitting with errors ", content)
        print("Errors", count)
        print(e)
        continue
        time.sleep(20)

    for i in range(len(newDictionary['results'])):
        dictionary_with_all = newDictionary['results'][i]
        images_info = dictionary_with_all['images']
        #print(images_info[0])

        for j in range(len(images_info)):
            dictionary_with_all_images_info = images_info[j]
            images_info_with_architectutre = dictionary_with_all_images_info['architecture']
            #print(images_info_with_architectutre)
            if images_info_with_architectutre.find('arm') != -1:
                print("Has arm " ,content)
                list_of_names_with_arm.append(content)
                count_of_arm = count_of_arm + 1
                bool_arm_not_found = False
                break
                #print("Has ARM")
        if bool_arm_not_found is False:
            break

print(len(list_of_names_with_arm))
print(list_of_names_with_arm)

print("================================")

print(len(list_with_errors))
print(list_with_errors)

with open('repos_list_with_arm.txt', 'w+') as f1:
    # write elements of list
    for items in list_of_names_with_arm:
        f1.write('%s\n' % items)

    print("Fixed repos_list")

#close the file
f1.close()

with open('repos_list_with_arm_errors.txt', 'w+') as f2:
    # write elements of list
    for items in list_with_errors:
        f2.write('%s\n' % items)

    print("Error list written")

#close the file
f2.close()