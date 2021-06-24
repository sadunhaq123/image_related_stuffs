import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections
import time

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

#erroneous_list2
Lines = open('snyk_all_commands_with_delete_commands_2.txt', 'r')

list_of_names = []
# Strips the newline character
for line in Lines:
    content = line.strip()
    print(content)
    if content[0] == 's':
        fixed_string = nth_repl(content, "/", "_", 3)
        print(fixed_string)
        list_of_names.append(fixed_string)
    else:
        list_of_names.append(content)


with open('snyk_all_commands_with_delete_commands_fixed_2.txt', 'w+') as f1:
    # write elements of list
    for items in list_of_names:
        f1.write('%s\n' % items)

    print("File for snyk_all_commands_with_delete_commands_fixed_2 written successfully")

# close the file
f1.close()

