"""
need pip3 install pyyaml
"""
import yaml
import csv
from collections import defaultdict

paper_year = defaultdict(int)

with open("data/Data_Cat.csv", "r") as csvdata:
    reader = csv.DictReader(csvdata)

    for paper in reader:
        bibkey = paper["Conference"] + str(paper["Year"])
        paper_year[bibkey] += 1
        output_format = {
            "layout": "publication",
            "title": paper["Title"],
            "conference": paper["Conference"],
            "year": int(paper["Year"]),
            "bibkey": bibkey + "_" + str(paper_year[bibkey])
        }
        with open(f"docs/_publications/{bibkey}_{paper_year[bibkey]}.md", "w") as yamldata:
            yamldata.write("---\n" + yaml.dump(output_format) + "---\n")