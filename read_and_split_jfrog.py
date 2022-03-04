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
jfrog_list_of_names_with_commands = []

count_for_docker_pull = 0
count_for_jfrog = 0
# Strips the newline character
for line in Lines:

    content = line.strip()
    name_with_tag = content
    print(name_with_tag)
    #print(type(name_with_publisher_but_without_count))
    #name_without_publisher_and_without_count = name_with_publisher_but_without_count.split('/')
    docker_pull_command = "docker pull " + name_with_tag
    name_with_tag_without_digest = name_with_tag.split('@')
    #print(name_with_tag_without_digest)
    jfrog_list_of_names_commands = "docker tag " + name_with_tag + " mdsadunutsatrial.jfrog.io/docker-local-arm/" + name_with_tag_without_digest[0] + "_arm"

    #list_of_names.insert(count, name_without_publisher_and_without_count[1])
    jfrog_push_commands = "docker push mdsadunutsatrial.jfrog.io/docker-local-arm/"  +  name_with_tag_without_digest[0] + "_arm"
    jfrog_list_of_names_with_commands.append(docker_pull_command)
    jfrog_list_of_names_with_commands.append(jfrog_list_of_names_commands)
    jfrog_list_of_names_with_commands.append(jfrog_push_commands)

    #list_of_docker_pull_commands.insert(count, docker_pull_command)
    #jfrog_list_of_names_with_commands.insert(count, jfrog_list_of_names_commands)
    #count_for_docker_pull += 1
    #print(name_without_publisher_and_without_count[1])
    #print("Line{}: {}".format(count, line.strip()))

#print(list_of_names_with_commands[0])
#print(list_of_names_with_commands[1])

with open('jfrog_official_digests_upto_1.txt', 'w+') as f:
    # write elements of list
    for items in jfrog_list_of_names_with_commands:
        f.write('%s\n' % items)

    print("File for JFrog written successfully")

# close the file
f.close()


with open('docker_pull_command_jfrog_official_digests_upto_1.txt', 'w+') as f:
    # write elements of list
    for items in list_of_docker_pull_commands:
        f.write('%s\n' % items)

    print("File for Docker Pull written successfully")

# close the file
f.close()