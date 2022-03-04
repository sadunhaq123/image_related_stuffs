file1 = open('official_digest_with_arm_two.txt', 'r')
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
    name_with_tag = content
    print(name_with_tag)
    #print(type(name_with_publisher_but_without_count))
    #name_without_publisher_and_without_count = name_with_publisher_but_without_count.split('/')
    docker_pull_command = "docker pull " + name_with_tag
    clair_list_of_names_commands = "./clair-scanner --ip 192.168.1.182 " + name_with_tag \
                               + " > clair_official_digests_tag_upto_1/" + name_with_tag + "_errors"
    #list_of_names.insert(count, name_without_publisher_and_without_count[1])
    list_of_docker_pull_commands.insert(count, docker_pull_command)
    clair_list_of_names_with_commands.insert(count, clair_list_of_names_commands)
    count += 1
    #print(name_without_publisher_and_without_count[1])
    #print("Line{}: {}".format(count, line.strip()))

#print(list_of_names_with_commands[0])
#print(list_of_names_with_commands[1])

counter_clair = 0
with open('clair_official_tag_digests_upto_1.txt', 'w+') as f:
    # write elements of list
    for items in clair_list_of_names_with_commands:
        f.write('%s\n' % items)
        counter_clair = counter_clair + 1

    print("File for Clair written successfully")

# close the file
f.close()


with open('docker_pull_command_official_digests_upto_1.txt', 'w+') as f:
    # write elements of list
    for items in list_of_docker_pull_commands:
        f.write('%s\n' % items)

    print("File for Docker Pull written successfully")

# close the file
f.close()