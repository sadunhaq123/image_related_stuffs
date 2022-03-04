file1 = open('most_recent_list_end_of_sept.txt', 'r')
Lines = file1.readlines()
list_of_names = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []
snyk_list_of_names  = []
list_of_docker_pull_commands = []

count = 0
# Strips the newline character
for line in Lines:

    content = line.strip()
    name_with_tag = content
    print(name_with_tag)
    name_without_colon = name_with_tag.replace(':', '_', 1)
    #print(type(name_with_publisher_but_without_count))
    snyk_pull_image_command = "snyk container test " + name_with_tag + " --json-file-output=snyk_latest_results_json_upto_1/" \
                              + name_without_colon + "_json"
    docker_pull_command = "docker pull " + name_with_tag
    snyk_list_of_names.append(snyk_pull_image_command)
    list_of_docker_pull_commands.append(docker_pull_command)
    #print(name_without_publisher_and_without_count[1])
    #print("Line{}: {}".format(count, line.strip()))

#print(list_of_names_with_commands[0])
#print(list_of_names_with_commands[1])

with open('snyk_command_for_json_upto_1.txt', 'w+') as f:
    # write elements of list
    for items in snyk_list_of_names:
        #if counter > 1000:
        #    break
        f.write('%s\n' % items)

    print("File for Snyk written successfully")

# close the file
f.close()

counter_trivy = 0
with open('docker_pull_commands_for_snyk.txt', 'w+') as f1:
    # write elements of list
    for items in list_of_docker_pull_commands:
        #if counter_trivy > 1000:
        #    break
        f1.write('%s\n' % items)

    print("File for Docker Snyk written successfully")

# close the file
f1.close()