import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections
import time

file1 = open('repos-list.txt', 'r')

#Lines = ['kubernetesui/dashboard']
Lines = file1.readlines()
list_of_names = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []
list_with_errors =[]
list_of_names_with_arm = []

def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    #print(find)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        #print(find)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        fixed_string = s[:find] + repl + s[find+len(sub):]
        #print(fixed_string)
        return s[:find] + repl + s[find+len(sub):]
    return s

count = 0
line_number=1
file_tracker_number=1
# Strips the newline character
for line in Lines:
    bool_arm_not_found = True
    content = line.strip()
    content_without_prefix = content[6:]
    print(content_without_prefix)
    content_without_prefix_fixed = nth_repl(content_without_prefix, '_', '/', 1)
    print(content_without_prefix_fixed)
    #break
    list_of_names.append(content_without_prefix_fixed)
    url = "https://hub.docker.com/v2/repositories/kubernetesui/dashboard/tags/?page=1"
    #url = "https://hub.docker.com/v2/repositories/" + content + "/tags/?page=1"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        newDictionary = json.loads(str(soup.text))
        print(soup.text)
        get_count = newDictionary['count']
        results = newDictionary['results']
        print(results[0])
        #print("Succesful Hits", content)
    except Exception as e:
        list_with_errors.append(content)
        print("Hitting with errors ", content)
        print("Errors", count)
        print(e)
        time.sleep(20)

    for i in range(len(newDictionary['results'])):
        dictionary_with_all = newDictionary['results'][i]
        images_info = dictionary_with_all['images']
        #print(images_info[0])

        for j in range(len(images_info)):
            dictionary_with_all_images_info = images_info[j]
            images_info_with_architectutre = dictionary_with_all_images_info['architecture']
            #print(images_info_with_architectutre)
            if images_info_with_architectutre.find('arm'):
                list_of_names_with_arm.appen(content_without_prefix_fixed)
                bool_arm_not_found = False
                break
                #print("Has ARM")
        if bool_arm_not_found is False:
            break


print(list_of_names_with_arm)

#with open('fixed_repos_list.txt', 'w+') as f1:
#    # write elements of list
#    for items in list_of_names:
#        f1.write('%s\n' % items)
#
#    print("Fixed repos_list")
#
# close the file
#f1.close()