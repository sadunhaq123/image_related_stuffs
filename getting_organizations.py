file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
list_of_names = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []
counting_dictionary = dict()

count = 0
# Strips the newline character
for line in Lines:

    content = line.strip()
    name_with_publisher_but_without_count = content.split('/')
    name_of_organization = name_with_publisher_but_without_count[0]
    print(name_of_organization)
    count = count + 1
    if name_of_organization in counting_dictionary:
            counting_dictionary[name_of_organization] =  counting_dictionary[name_of_organization] + 1
            #print ("Got name " +name_of_organization+ "again")
    else:
            counting_dictionary[name_of_organization]  = 1
            #print("Got new name " + name_of_organization)
    #print(type(name_with_publisher_but_without_count))
    #name_without_publisher_and_without_count = name_with_publisher_but_without_count.split('/')


print(counting_dictionary)
print(count)

with open("list_of_organizations.txt", 'w') as f:
    for key, value in counting_dictionary.items():
        f.write('%s\n' % key)