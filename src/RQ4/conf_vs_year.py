import csv

journals = ["TOSEM", "EMSE","TSE", "IST"]
conferences = ["ICSE", "MSR", "ICSME", "FSE", "ASE"]

with open("Excel_data/paper_names_premium.csv", "r") as papers_file:
    papers = csv.DictReader(papers_file)
    type_count = {}
    type_count2 = {}


    for paper in papers:
        concrete_conf = paper["Conference"] if paper["Conference"] in journals + conferences else "Other"
        conf = "Conference" if paper["Conference"] in conferences else "Journal" if paper["Conference"] in journals else "Other"
        year = paper["Year"] if int(paper["Year"]) > 2008 else "~2008"
        type_set = year +","+ conf
        type_set2 = year+","+ conf+","+concrete_conf

        if type_set not in type_count:
            type_count[type_set] = 1
        else:
            type_count[type_set] = type_count[type_set] + 1
        if type_set2 not in type_count2:
            type_count2[type_set2] = 1
        else:
            type_count2[type_set2] = type_count2[type_set2] + 1



with open("Excel_data/paper_names_snowballed.csv", "r") as papers_file:
    papers = csv.DictReader(papers_file)

    for paper in papers:
        concrete_conf = paper["Conference"] if paper["Conference"] in journals + conferences else "Other"
        conf = "Conference" if paper["Conference"] in conferences else "Journal" if paper["Conference"] in journals else "Snowball"
        # conf = "Conference" if paper["Conference"] in conferences else "Journal" if paper["Conference"] in journals else "Other"
        year = paper["Year"] if int(paper["Year"]) > 2008 else "~2008"
        type_set = year +","+ conf
        type_set2 = year+","+ conf+","+concrete_conf

        if type_set not in type_count:
            type_count[type_set] = 1
        else:
            type_count[type_set] = type_count[type_set] + 1
        if type_set2 not in type_count2:
            type_count2[type_set2] = 1
        else:
            type_count2[type_set2] = type_count2[type_set2] + 1

with open("Excel_data/year_vs_conf.csv", "w") as target:
    writer = csv.writer(target)
    writer.writerow(["Year","Publication","Count"])
    for content, count in type_count.items():
        writer.writerow(content.split(",") + [str(count)])

with open("Excel_data/year_vs_conf2.csv", "w") as target:
    writer = csv.writer(target)
    writer.writerow(["Year","Type","Publication","Count"])
    for content, count in type_count2.items():
        writer.writerow(content.split(",") + [str(count)])


