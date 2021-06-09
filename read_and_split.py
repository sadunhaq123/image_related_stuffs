file1 = open('myfile.txt', 'r')
Lines = file1.readlines()
list_of_names = []
trivy_list_of_names_with_commands = []
snyk_list_of_names_with_commands = []
docker_list_image_rm_command = []
snyk_list_of_names_with_delete_commands = []

count = 0
# Strips the newline character
for line in Lines:

    content = line.strip()
    name_with_publisher_but_without_count = content.split(':')
    print(name_with_publisher_but_without_count[0])
    name_without_publisher_and_without_count = name_with_publisher_but_without_count[0].split('/')
    trivy_pull_image_command = "trivy image --skip-update " + name_with_publisher_but_without_count[0] \
                               + " > trivy_top_thousand/" + name_without_publisher_and_without_count[0] + "_errors"
    snyk_pull_image_command = "snyk container test " + name_with_publisher_but_without_count[0] \
                               + " > snyk_top_thousand/" + name_without_publisher_and_without_count[0] + "_errors"
    docker_image_rm_command = "docker image rm " + name_with_publisher_but_without_count[0] \
                              + " > docker_rm_logs/" + name_without_publisher_and_without_count[0] + "_errors"
    #list_of_names.insert(count, name_without_publisher_and_without_count[1])
    trivy_list_of_names_with_commands.insert(count, trivy_pull_image_command)
    #snyk_list_of_names_with_commands.insert(count, snyk_pull_image_command)
    snyk_list_of_names_with_delete_commands.insert(count, snyk_pull_image_command)
    count += 1
    snyk_list_of_names_with_delete_commands.insert(count, docker_image_rm_command)
    count += 1
    #print(name_without_publisher_and_without_count[1])
    #print("Line{}: {}".format(count, line.strip()))

#print(list_of_names_with_commands[0])
#print(list_of_names_with_commands[1])

counter = 0
with open('snyk_top_commands_with_delete_commands.txt', 'w+') as f:
    # write elements of list
    for items in snyk_list_of_names_with_delete_commands:
        if counter > 1000:
            break
        f.write('%s\n' % items)
        counter = counter + 1

    print("File for Snyk written successfully")

# close the file
f.close()

counter_trivy = 0
with open('trivy_top_commands.txt', 'w+') as f1:
    # write elements of list
    for items in trivy_list_of_names_with_commands:
        if counter_trivy > 1000:
            break
        f1.write('%s\n' % items)
        counter_trivy = counter_trivy + 1

    print("File for Trivy written successfully")

# close the file
f1.close()