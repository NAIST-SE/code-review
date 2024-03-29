"""
require: pip3 install pyyaml
"""
import csv
from yaml import dump

with open("data/Replicated.csv", "r") as csvdata:
    reader = csv.DictReader(csvdata)


    with open("data/Data_Cat.csv", "r") as csvdata:
        papers = list(csv.DictReader(csvdata))

        for data in reader:
            id = data["PaperId"]
            titles = [x for x in papers if x['No'] == data['PaperId']]

            output_format = {
                "title": "" if len(titles) == 0 else titles[0]['Title'],
                "id": id,
                "publication_id": id,
                "link": data["link"] if "link" in data else "---",
                "source": data["source"] if "source" in data and data["source"] != ""  else "---",
                "host": data["host"] if "host" in data and data["host"] != "" else "---",
                "available": data["available"],
                "type": data["type"] if "type" in data and data["type"] != "null" else "---",
            }
            with open(f"docs/_dataset/{id}.md", "w") as yamldata:
                yamldata.write("---\n" + dump(output_format) + "---\n")