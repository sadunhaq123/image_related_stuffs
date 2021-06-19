import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import collections



file1 = open('random_word_list.txt', 'r')
Lines = file1.readlines()
list_of_names = []
list_of_names_split_one = []
list_of_names_split_two = []
list_of_names_split_three = []
list_of_names_split_four = []
list_of_names_split_five = []
list_of_names_split_six = []
list_of_names_split_seven = []
list_of_names_split_eight = []
list_of_names_split_nine = []
list_of_names_split_ten = []
list_with_hits = []
list_with_errors = []
line_number = 0
count = 0
successful_hits = 0
# Strips the newline character
for line in Lines:
    content = line.strip()
    if line_number < 100001:
        list_of_names_split_one.append(content)
    elif line_number > 100000 and line_number < 200001:
        list_of_names_split_two.append(content)
    elif line_number > 200000 and line_number < 300001:
        list_of_names_split_three.append(content)
    elif line_number > 300000 and line_number < 400001:
        list_of_names_split_four.append(content)
    elif line_number > 400000 and line_number < 500001:
        list_of_names_split_five.append(content)
    elif line_number > 500000 and line_number < 600001:
        list_of_names_split_six.append(content)
    elif line_number > 600000 and line_number < 700001:
        list_of_names_split_seven.append(content)
    elif line_number > 700000 and line_number < 800001:
        list_of_names_split_eight.append(content)
    line_number = line_number + 1

with open('list_of_names_split_one.txt', 'w+') as f1:
    # write elements of list
    for items in list_of_names_split_one:
        f1.write('%s\n' % items)

    print("File for list_of_names_split_one written successfully")

# close the file
f1.close()

with open('list_of_names_split_two.txt', 'w+') as f2:
    # write elements of list
    for items in list_of_names_split_two:
        f2.write('%s\n' % items)

    print("File for list_of_names_split_two written successfully")

# close the file
f2.close()

with open('list_of_names_split_three.txt', 'w+') as f3:
    # write elements of list
    for items in list_of_names_split_three:
        f3.write('%s\n' % items)

    print("File for list_of_names_split_threes written successfully")

# close the file
f3.close()

with open('list_of_names_split_four.txt', 'w+') as f4:
    # write elements of list
    for items in list_of_names_split_four:
        f4.write('%s\n' % items)

    print("File for list_of_names_split_four written successfully")

# close the file
f4.close()

with open('list_of_names_split_five.txt', 'w+') as f5:
    # write elements of list
    for items in list_of_names_split_five:
        f5.write('%s\n' % items)

    print("File for list_of_names_split_five written successfully")

# close the file
f5.close()

with open('list_of_names_split_six.txt', 'w+') as f6:
    # write elements of list
    for items in list_of_names_split_six:
        f6.write('%s\n' % items)

    print("File for list_of_names_split_six written successfully")

# close the file
f6.close()

with open('list_of_names_split_seven.txt', 'w+') as f7:
    # write elements of list
    for items in list_of_names_split_seven:
        f7.write('%s\n' % items)

    print("File for list_of_names_split_seven written successfully")

# close the file
f7.close()

with open('list_of_names_split_eight.txt', 'w+') as f8:
    # write elements of list
    for items in list_of_names_split_eight:
        f8.write('%s\n' % items)

    print("File for list_of_names_split_eight written successfully")

# close the file
f8.close()