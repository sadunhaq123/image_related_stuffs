import json
import xlsxwriter
import os
import csv

file_list = open('list_of_files_trivy_json.txt', 'r')
reading_file_lists = file_list.readlines()

for first_line in reading_file_lists:
    content_first = first_line.strip()
    index_of_last_underscore = content_first.rfind('_')
    #json_file_name_with_underscore = content_first.split('_')
    json_file_name = content_first[:index_of_last_underscore]
    #print(json_file_name)

    #workbook = xlsxwriter.Workbook('trivy_officials_first_json/trivy_' +json_file_name +'_from_json_errors.xlsx')
    #worksheet = workbook.add_worksheet()

    row = 0
    list_without_headings = []
    flag_found_json_bracket = False
    flag_file_empty_errors = False
    first_name_and_target = True

    name_and_tag_list = []
    target_list = []
    type_list = []
    vuln_id_list = []
    package_name_list = []
    installed_version_list = []
    fixed_version_list = []
    primary_url_list = []
    title_list = []
    description_list = []
    severity_list = []

    file1 = open('trivy_officials_first_json/' +json_file_name+ '_errors.json','r', encoding='utf-8')
    Lines = file1.readlines()

    for line in Lines:

        content = line.strip()
        name_with_tag = content
        #print(content)
        if content == 'null':
            flag_file_empty_errors = True
        if (content[0] == '['):
            flag_found_json_bracket = True

        if (flag_found_json_bracket is True):
            list_without_headings.append(content)
        elif (flag_found_json_bracket is False):
            continue

    if flag_file_empty_errors is True:
        continue

    with open('trivy_officials_first_json/'+json_file_name+'_latest_errors_without_header.json', 'w+') as f:
        # write elements of list
        for items in list_without_headings:
            f.write('%s\n' % items)

        print("File without header written successfully")

    # close the file
    f.close()



    if os.stat('trivy_officials_first_json/' +json_file_name+ '_latest_errors_without_header.json').st_size == 0:
        continue
    file2 = open('trivy_officials_first_json/' +json_file_name+ '_latest_errors_without_header.json', 'r')
    data = json.load(file2)

    #print(data)
    #print(type(data))

    for i in range(len(data)):
        target = data[i]["Target"]
        if first_name_and_target is True:
            first_name_and_tag = target
            print(first_name_and_tag)
            first_name_and_target = False

        target_type = data[i]["Type"]
        # print(data[i]["Target"])
        #print(data[i]["Vulnerabilities"])
        vulnerabilities = data[i]["Vulnerabilities"]
        if vulnerabilities is None:
            continue
        for j in range(len(vulnerabilities)):
            full_vulnerability_block = vulnerabilities[j]
            vuln_id = full_vulnerability_block["VulnerabilityID"]
            package_name = full_vulnerability_block["PkgName"]
            installed_version = full_vulnerability_block["InstalledVersion"]
            try:
                fixed_version = full_vulnerability_block["FixedVersion"]
            except KeyError:
                fixed_version = None
            try:
                primary_url = full_vulnerability_block["PrimaryURL"]
            except KeyError:
                primary_url = None
            try:
                title = full_vulnerability_block["Title"]
            except KeyError:
                title = None
            try:
                description = full_vulnerability_block["Description"]
            except KeyError:
                description = None
            severity = full_vulnerability_block["Severity"]
            #print(vuln_id + " " + package_name + " " + installed_version + " " + fixed_version + " " + primary_url + " " + title + " " + description + " " + severity)
            name_and_tag_list.append(first_name_and_tag)
            target_list.append(target)
            type_list.append(target_type)
            vuln_id_list.append(vuln_id)
            package_name_list.append(package_name)
            installed_version_list.append(installed_version)
            fixed_version_list.append(fixed_version)
            primary_url_list.append(primary_url)
            title_list.append(title)
            description_list.append(description)
            severity_list.append(severity)

    with open('trivy_combined_result_revised.csv', 'a') as result_file:
        writer = csv.writer(result_file, dialect='excel')

        for w in range(len(name_and_tag_list)):
            writer.writerow([name_and_tag_list[w]
                            ,target_list[w]
                            ,type_list[w]
                            ,vuln_id_list[w]
                            ,package_name_list[w]
                            ,severity_list[w]
                            ,installed_version_list[w]
                            ,fixed_version_list[w]
                            ,primary_url_list[w]
                            ,title_list[w]
                            ,description_list[w]])

    result_file.close()



#print(data["Target"])