file1 = open('official_digest_with_arm_three.txt', 'r')
Lines = file1.readlines()
list_of_names = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []
clair_list_of_names_with_commands = []
anchore_list_of_names_with_commands = []
jfrog_list_of_names_with_commands = []
clair_list_of_names_with_docker_pull_commands = []
list_of_docker_pull_commands = []
clair_list_of_names_with_commands = []

count = 0
# Strips the newline character
for line in Lines:

    content = line.strip()
    name_with_tag_and_sha = content
    #print(name_with_tag_and_sha)
    name_with_tag_only = name_with_tag_and_sha.split('@')
    #print(name_with_tag_only[0])
    list_of_names.append(name_with_tag_only[0])

with open('most_recent_list_end_of_sept.txt', 'w+') as f:
    # write elements of list
    for items in list_of_names:
        #if counter > 1000:
        #    break
        f.write('%s\n' % items)
        #counter = counter + 1

    print("File written successfully")

# close the file
f.close()

